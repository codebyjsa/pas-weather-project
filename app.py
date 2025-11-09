import pandas as pd
import io
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from weather_analysis import analyze_weather_data

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'  # Required for flash messages

# Configure settings
ALLOWED_EXTENSIONS = {'csv'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_csv(file_stream):
    """
    Validate CSV file has required columns and correct format.
    Args:
        file_stream: File object or BytesIO stream
    Returns (is_valid, error_message, dataframe)
    """
    try:
        # Try to read the CSV from stream
        df = pd.read_csv(file_stream)
        
        # Check if required columns exist
        required_columns = ['Date', 'Temperature', 'Rainfall']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            return False, f"Missing required columns: {', '.join(missing_columns)}", None
        
        # Check if DataFrame is empty
        if df.empty:
            return False, "CSV file is empty", None
        
        # Try to parse dates
        try:
            pd.to_datetime(df['Date'])
        except Exception:
            return False, "Invalid date format in 'Date' column. Use format like YYYY-MM-DD", None
        
        # Check if Temperature and Rainfall are numeric
        try:
            pd.to_numeric(df['Temperature'])
        except Exception:
            return False, "'Temperature' column must contain numeric values", None
        
        try:
            pd.to_numeric(df['Rainfall'])
        except Exception:
            return False, "'Rainfall' column must contain numeric values", None
        
        return True, None, df
        
    except pd.errors.EmptyDataError:
        return False, "CSV file is empty or corrupted", None
    except pd.errors.ParserError:
        return False, "Unable to parse CSV file. Please check the file format", None
    except Exception as e:
        return False, f"Error reading CSV file: {str(e)}", None

@app.route('/')
def index():
    """Landing page with file upload form"""
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload or manual CSV text input and process in memory"""
    
    # Check if user provided CSV text manually
    csv_text = request.form.get('csv_text', '').strip()
    
    if csv_text:
        # Handle manual CSV text input
        try:
            # Create file stream from text
            text_stream = io.StringIO(csv_text)
            
            # Validate CSV
            is_valid, error_message, df = validate_csv(text_stream)
            
            if not is_valid:
                flash(f'Invalid CSV data: {error_message}', 'danger')
                return redirect(url_for('index'))
            
            # Convert DataFrame to CSV string and store in session
            csv_string = df.to_csv(index=False)
            session['csv_data'] = csv_string
            session['filename'] = 'manual_input.csv'
            
            flash('CSV data processed successfully!', 'success')
            return redirect(url_for('results'))
            
        except Exception as e:
            flash(f'Error processing CSV text: {str(e)}', 'danger')
            return redirect(url_for('index'))
    
    # Handle file upload
    if 'file' not in request.files:
        flash('No file or CSV data provided', 'danger')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected', 'danger')
        return redirect(url_for('index'))
    
    if not allowed_file(file.filename):
        flash('Invalid file type. Please upload a CSV file', 'danger')
        return redirect(url_for('index'))
    
    if file:
        filename = secure_filename(file.filename)
        
        # Read file content into memory
        file_content = file.read()
        file_stream = io.BytesIO(file_content)
        
        # Validate CSV file
        is_valid, error_message, df = validate_csv(file_stream)
        
        if not is_valid:
            flash(f'Invalid CSV file: {error_message}', 'danger')
            return redirect(url_for('index'))
        
        # Convert DataFrame to CSV string and store in session
        csv_string = df.to_csv(index=False)
        session['csv_data'] = csv_string
        session['filename'] = filename
        
        flash('File uploaded successfully!', 'success')
        return redirect(url_for('results'))
    
    flash('Error uploading file', 'danger')
    return redirect(url_for('index'))

@app.route('/results')
def results():
    """Display analysis results from session data"""
    # Check if CSV data exists in session
    if 'csv_data' not in session or 'filename' not in session:
        flash('No data to analyze. Please upload a CSV file.', 'warning')
        return redirect(url_for('index'))
    
    try:
        # Get data from session
        csv_data = session['csv_data']
        filename = session['filename']
        
        # Convert CSV string back to file-like object
        csv_stream = io.StringIO(csv_data)
        
        # Analyze the data
        analysis_data = analyze_weather_data(csv_stream)
        return render_template('results.html', data=analysis_data, filename=filename)
    except Exception as e:
        flash(f"Error analyzing file: {str(e)}", 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
