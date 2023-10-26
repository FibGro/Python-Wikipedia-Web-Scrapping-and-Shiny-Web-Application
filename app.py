

#----------------------------------------------
# Import all the library 
#----------------------------------------------

from shiny import App, Inputs, Outputs, Session, render, ui
from shinywidgets import output_widget, render_widget
import plotly.express as px
import plotly.io as pio
import pandas as pd
from pathlib import Path

#----------------------------------------------
# Upload the file 
#----------------------------------------------

infile = Path(__file__).parent / "df.csv"
df = pd.read_csv(infile)

#----------------------------------------------
# Define Global
#----------------------------------------------

#groupby based on headquarter_location and then sum all revenue for each country. 
#then, sort the dataframe with decending order based on the revenue_$
#assign it as variable num_1
#add new coloumn to check the percentage of revenue
num_1 = df.groupby('headquarter_location')[['revenue', 'profit', 'employee_number' ]].sum().reset_index().sort_values('revenue', ascending=False)
num_1['perc_rev'] = (num_1['revenue']*100/(num_1['revenue'].sum())).round(2)


#groupby based on headquarter_location and then sum all revenue for each country. 
#then, sort the dataframe with decending order based on the revenue_$
#add new coloumn to check the percentage of employee
num_2 = df.groupby('industry')[['revenue', 'profit', 'employee_number' ]].sum().reset_index().sort_values('revenue', ascending=False)
num_2['perc_emp'] = (num_2['employee_number']*100/(num_2['employee_number'].sum())).round(2)

#----------------------------------------------
# Define User Interaction (ui)
#----------------------------------------------

#Main navigation (page navbar)
app_ui = ui.page_navbar(

#----------------------------------------------
# First Tab : Overview
#----------------------------------------------

    ui.nav(
    ui.h2({"style": "text-align: center; font-size : 28px; color :white; font-weight:bold; margin: 0 15px;"}, "Overview"),
    
        #First page : Layout sidebar
        ui.layout_sidebar(
        
        #First page : panel sidebar
        ui.panel_sidebar(
          
            {"style": "background-color: #023047 ; font-size : 17px ; color:white ; height:700px"},
            ui.tags.style("""body {font-family: Optima}"""),
        
            ui.br(),
            ui.p('''
                This dataset, retrieved from Wikipedia, comprises the world's largest companies ranked by 
                consolidated revenue in the Fortune Global 500 2023 rankings. The list is limited to the 
                top 50 companies, all of which have annual revenues exceeding US$130 billion.'''),
            ui.br(),
            ui.p('''          
                You can explore 
                the scatter plot by selecting the industry type and specifying the revenue range. On the chart, 
                the x-axis represents revenue, the y-axis represents profit, and the size of the bubble 
                corresponds to the number of employees.
                '''),
            ui.br(),
            
            #Input selectize 
            ui.input_selectize("industry", "Choose Type of Industry (One or Multiple) :",
                    {"Oil and gas": "Oil and gas",
                    "Healthcare": "Healthcare",
                    "Retail":"Retail",
                    "Financials":"Financials",
                    "Commodities":"Commodities",
                    "Automotive":"Automotive",
                    "Electronics":"Electronics",
                    "Electricity": "Electricity"},
                    multiple = True),

            #Input slider
            ui.input_slider("revenue", 
                "Choose Range of Revenue :", 
                 min = 157000, max = 612000, value=[157000, 612000]),
            ),

        #First page : Main pane;
        ui.panel_main(
            
            #Output : scatterplot
            output_widget("scatter_1"),
            {"style":  "height:700px"}
            )
        )),
    

#----------------------------------------------
# Second Tab : Map
#----------------------------------------------

    ui.nav(
    ui.h2({"style": "text-align: center; font-size : 28px; color :white; font-weight:bold; margin: 0 15px;"}, "Map"),
    
        #Second Tab : Layout Sidebar
        ui.layout_sidebar(
        
            #Second Tab : Panel Sidebar
            ui.panel_sidebar(
                {"style": "background-color: #023047 ; font-size : 17px ; color:white ; height:700px"},
                ui.tags.style("""body {font-family: Optima}"""),
        
                ui.br(),
                ui.p(''' 
                    In this section, we can examine the distribution of cumulative revenue, profit, and 
                    employee numbers based on headquarter location using a map. The map utilizes color to 
                    represent the values of each selected parameter, where darker colors indicate higher 
                    values compared to lighter colors. Simply choose one of the buttons to visualize the results.
                    '''),
                ui.br(),
                ui.br(),

                #Input : radio buttons
                ui.input_radio_buttons(
                    "parameter",
                    "Choose one parameter:",
                    {
                    "revenue":  "Revenue",
                    "profit": "Profit",
                    "employee_number": "Number of Employee"
                    }),
            ),

            #Second page : Main panel 
            ui.panel_main(
                {"style":  "height:700px"},
                
                #Output : text
                ui.output_text("txt"),
                
                #Output : map
                output_widget("map"),
                
                #style="font:Optima; background-color: white;",
                ),
                )),
    
#----------------------------------------------
# Third Tab : Dataset
#----------------------------------------------

    ui.nav(
    ui.h2({"style": "text-align: center; font-size : 28px; color :white; font-weight:bold; margin: 0 15px;"}, "Dataset"),

        # Third Tab : Layout sidebar
        ui.layout_sidebar(
            
            #Third Tab : Panel Sidebar
            ui.panel_sidebar(
     
                {"style": "background-color: #023047 ; font-size : 17px ; color:white ; height:700px"},
                ui.tags.style("""body {font-family: Optima}"""),
                ui.br(),
                ui.p('''
                    Here is the dataset for building the graph and map. You can observe the min and max 
                    values of revenue, profit, and the number of employees by enabling the buttons 
                    above the tables. 
                    '''),
                ui.br(),
                ui.p('''
                    Additionally, you can download the dataset by simply clicking the download button below. 
                    The source code for this project is available on GitHub, and you can find it in the 
                    'Source Code' tab.
                    '''),

                #Input : download box
                ui.download_button("download1", "Download CSV"), 
                ui.br(),
                ui.br(),
                ),

            #Third Tab : Main Panel
            ui.panel_main( 
                {"style":  "height:700px"},
                
                #Input : Checkbox
                ui.input_checkbox("highlight", "Highlight Min and Max Values"),
                
                #Output : Table
                ui.output_table("result"),

                #Output : Highlight
                ui.panel_conditional(
                    "input.highlight",
            
                #Text notify color
                ui.panel_absolute(
                    "Chocolate is Maximum, Grey is Minimum",
                    bottom="6px",
                    right="6px",
                    class_="p-1 bg-light border",
                    ),
            ),
                    #class_="p-3",

            ))),


#----------------------------------------------
# Fouth Tab : Source Code
#----------------------------------------------
    
    #Space between tab
    ui.nav_spacer(),
    
    #Fouth tab : Source Code
    ui.nav_control(
        
        #Direct to link
        ui.a("Source Code", 
            href="https://github.com/FibGro/Python-Wikipedia-Web-Scrapping-and-Shiny-Web-Application", 
            target="_blank", 
            style = "font: Optima; font-size: 28px; color: #e0a100; font-weight:bold ; margin-top: -4px;"),
        ),
    
#----------------------------------------------
# Update Layout : Tab
#----------------------------------------------

#Background for Tab (Weird that it notify in the last!!)
bg="#425236",
)

#----------------------------------------------
# Define Server
#----------------------------------------------

#Note : I did not make it in the sequence 
def server(input, output, session):
    
    #The table
    @output
    @render.table
    def table():
        infile = Path(__file__).parent / "df.csv"
        df = pd.read_csv(infile)
        return df


    #The scatterplot
    @output
    @render_widget
    def scatter_1():
        fig = px.scatter(
                 df.loc[(df.industry.isin(input.industry())) & (df.revenue < int(max(input.revenue()))) & (df.revenue > int(min(input.revenue()))) ],
                 x="revenue", 
                 y="profit", 
                 size="employee_number", 
                 color="industry",
                 title='Revenue, Profit, Employee Number and Industry Types',
                 size_max=60,
                 hover_name="companies_name", 
                 hover_data=["revenue", "profit", "employee_number", "industry"],
                 width = 900,
                 height = 630,
                 labels={"industry": "Type of Industry",
                         "revenue" : 'Revenue (USD)',
                         "profit" : 'Profit (USD)'})

        fig.update_layout(
            title=dict(font=dict(size=25)),
            title_font_color="black",
            font_family="Optima",
            font_color="black",
            title_font_family="Optima",
            legend_title_font_color="black",
            template = 'simple_white',
            hoverlabel=dict(
                font=dict(family="Optima", 
                 color="white")),
            )
        return fig

    #The map
    @output
    @render_widget
    def map():
        fig_1 = px.choropleth(num_1, 
                    locations='headquarter_location', 
                    locationmode='country names', 
                    color= input.parameter(),
                    color_continuous_scale='gnbu',
                    hover_name="headquarter_location", 
                    hover_data=["revenue", "profit", "employee_number"],
                    labels={input.parameter():input.parameter().capitalize()})

        fig_1.update_layout(
            title_font_color="black",
            font_family="Optima",
            font_color="black",
            title_font_family="Optima",
            legend_title_font_color="black",
            template = 'simple_white',
            autosize=False,
            margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            hoverlabel=dict(
                font=dict(family="Optima", 
                color="white")),
            width=900,
            height=500,
        )
        return fig_1

    #The download box
    @session.download()
    def download1():
        path = Path(__file__).parent / "df.csv"
        return str(path)


    #The text
    @output
    @render.text
    def txt():
        return '''
        It is evident that companies positioned within the top 50, with their headquarters 
        based in the United States, outshine their counterparts in other geographical regions 
        in terms of revenue, profit and number of employees. This observation underscores the prominence of U.S.-based companies 
        in this elite group, emphasizing their substantial share of the total pie. 
        Similarly, China emerged as a key player, making a noteworthy contribution to the 
        cumulative revenue, profit and employee number generated by these top companies.
        '''


    #Render Table
    @output
    @render.table
    def result():
        if not input.highlight():
            return df
        else:
            return (
                df.style.set_table_attributes(
                    'class="dataframe shiny-table table w-auto"'
                )
                .hide(axis="index")
                .set_table_styles(
                    [dict(selector="th", props=[("text-align", "right")])]
                )
                .highlight_min(color="#BFB68A", subset=['revenue', 'profit','employee_number'])
                .highlight_max(color="#BF7839", subset=['revenue', 'profit','employee_number'])
                )

#----------------------------------------------
# Define App
#----------------------------------------------

app = App(app_ui, server)