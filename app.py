from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 데이터 로드
df = px.data.gapminder()
# Dash 애플리케이션 생성
app = Dash(__name__)

# Layout 정의: 그래프 추가
app.layout = html.Div(
	style={'padding':'20px', 'font-family':'Arial'}, 
	children=[
		html.H1('국가별 GDP 변화' ,style={'color':'blue'}),
		dcc.Dropdown(
			id='country-dropdown',
			options=[{'label':country, 'value':country} for country in df['country'].unique()],
			value='Canada',
			style={'width':'50%', 'margin-bottom':'20px'}
		),
		dcc.Graph(id='gdp-graph')
	])


@app.callback(
	Output('gdp-graph', 'figure'),
	Input('country-dropdown','value')
)
def udpate_graph(selected_country):
	filtered_df = df[df['country']==selected_country]
	fig = px.line(filtered_df, x='year', y='gdpPercap', title=f'{selected_country}의 GDP 변화')
	return fig


if __name__ == '__main__':
	app.run(debug=False)
