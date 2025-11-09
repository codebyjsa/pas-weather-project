import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

def analyze_weather_data(csv_file_stream):
    """
    Analyzes weather data and returns statistics and interactive charts.
    
    Args:
        csv_file_stream: File-like object (stream) containing CSV data
    
    Returns a dictionary containing all analysis results.
    Raises ValueError if data processing fails.
    """
    try:
        # Load the CSV from stream
        df = pd.read_csv(csv_file_stream, parse_dates=['Date'])
        
        # Extract month for analysis
        df['Month'] = df['Date'].dt.month
        
        # Calculate descriptive statistics
        if df['Temperature'].mode().empty:
            mode_temp = df['Temperature'].median()  # Fallback if no mode
        else:
            mode_temp = df['Temperature'].mode()[0]
            
        temp_stats = {
            'mean': round(df['Temperature'].mean(), 2),
            'median': round(df['Temperature'].median(), 2),
            'mode': round(mode_temp, 2),
            'std': round(df['Temperature'].std(), 2)
        }
        
        # Monthly summary
        monthly_stats = df.groupby('Month')['Temperature'].agg(['mean', 'std', 'min', 'max'])
        monthly_stats = monthly_stats.round(2)
        monthly_table = monthly_stats.to_html(classes='table table-striped', border=0)
        
        # ANOVA Test
        groups = [group['Temperature'].values for name, group in df.groupby('Month')]
        if len(groups) < 2:
            # Not enough groups for ANOVA
            anova_result = {
                'f_stat': 0.0,
                'p_value': 1.0,
                'significant': False
            }
        else:
            f_stat, p_value = stats.f_oneway(*groups)
            anova_result = {
                'f_stat': round(f_stat, 3),
                'p_value': round(p_value, 4),
                'significant': p_value < 0.05
            }
        
        # Create interactive plots
        
        # 1. Daily Temperature Trend
        temp_trend = go.Figure()
        temp_trend.add_trace(go.Scatter(
            x=df['Date'],
            y=df['Temperature'],
            mode='lines',
            name='Temperature',
            line=dict(color='teal', width=2)
        ))
        temp_trend.update_layout(
            title='Daily Temperature Trend',
            xaxis_title='Date',
            yaxis_title='Temperature (°C)',
            hovermode='x unified',
            template='plotly_white'
        )
        temp_trend_html = temp_trend.to_html(full_html=False, include_plotlyjs='cdn')
        
        # 2. Monthly Average Bar Chart
        monthly_avg = df.groupby('Month')['Temperature'].mean().reset_index()
        bar_chart = go.Figure()
        bar_chart.add_trace(go.Bar(
            x=monthly_avg['Month'],
            y=monthly_avg['Temperature'],
            marker_color='orange',
            name='Avg Temperature'
        ))
        bar_chart.update_layout(
            title='Average Temperature by Month',
            xaxis_title='Month',
            yaxis_title='Temperature (°C)',
            template='plotly_white'
        )
        bar_chart_html = bar_chart.to_html(full_html=False, include_plotlyjs='cdn')
        
        # 3. Daily Rainfall Trend
        rainfall_trend = go.Figure()
        rainfall_trend.add_trace(go.Scatter(
            x=df['Date'],
            y=df['Rainfall'],
            mode='lines',
            name='Rainfall',
            line=dict(color='blue', width=2),
            fill='tozeroy',
            fillcolor='rgba(0, 0, 255, 0.1)'
        ))
        rainfall_trend.update_layout(
            title='Daily Rainfall Trend',
            xaxis_title='Date',
            yaxis_title='Rainfall (mm)',
            hovermode='x unified',
            template='plotly_white'
        )
        rainfall_trend_html = rainfall_trend.to_html(full_html=False, include_plotlyjs='cdn')
        
        # Return all data
        return {
            'temp_stats': temp_stats,
            'monthly_table': monthly_table,
            'anova': anova_result,
            'temp_trend_chart': temp_trend_html,
            'bar_chart': bar_chart_html,
            'rainfall_chart': rainfall_trend_html
        }
        
    except KeyError as e:
        raise ValueError(f"Missing required column in CSV: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Data processing error: {str(e)}")
    except Exception as e:
        raise ValueError(f"Unexpected error analyzing data: {str(e)}")
