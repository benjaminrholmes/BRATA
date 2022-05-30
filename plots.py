from pydataset import data
import plotly.graph_objects as go

iris = data('iris')


def iris_scatter(data):
    iris = data.rename({"Sepal.Length": "SepalLengthCm",
                        "Sepal.Width": "SepalWidthCm",
                        "Petal.Length": "PetalLengthCm",
                        "Petal.Width": "PetalWidthCm"}, axis=1)

    setosa = iris.loc[iris["Species"] == "setosa"]
    versicolor = iris.loc[iris["Species"] == "versicolor"]
    virginica = iris.loc[iris["Species"] == "virginica"]

    # list of column names
    spcols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    # empty lists for calcs
    setosa_spavg = ["Setosa"]
    versicolor_spavg = ["Versicolor"]
    virginica_spavg = ["Virginica"]
    # setosa calc
    for i in spcols:
        x = round(setosa[i].mean(), 1)
        setosa_spavg.append(x)
    # versicolor calc
    for i in spcols:
        x = round(versicolor[i].mean(), 1)
        versicolor_spavg.append(x)
    # virginica calc
    for i in spcols:
        x = round(virginica[i].mean(), 1)
        virginica_spavg.append(x)
    # reviewing calc results

    # adding figure for Length/Width visualization
    fig1 = go.Figure()
    # adding traces
    fig1.add_trace(go.Scatter(x=setosa.SepalWidthCm, y=setosa.SepalLengthCm, name='Setosa',
                              mode='markers', marker_color='rgb(154, 79, 219)', marker_opacity=0.8,
                              hovertemplate="<b>SepalWidthCm:</b> %{x} <br><b>SepalLengthCm:</b> %{y}"))
    fig1.add_trace(go.Scatter(x=versicolor.SepalWidthCm, y=versicolor.SepalLengthCm, name='Versicolor',
                              mode='markers', marker_color='rgb(79, 196, 219)', marker_opacity=0.8,
                              hovertemplate="<b>SepalWidthCm:</b> %{x} <br><b>SepalLengthCm:</b> %{y}"))
    fig1.add_trace(go.Scatter(x=virginica.SepalWidthCm, y=virginica.SepalLengthCm, name='Virginica',
                              mode='markers', marker_color='rgb(225, 69, 69)', marker_opacity=0.8,
                              hovertemplate="<b>SepalWidthCm:</b> %{x} <br><b>SepalLengthCm:</b> %{y}"))
    # # Add shapes
    # fig1.add_shape(type="circle",
    #               xref="x", yref="y",
    #               x0=min(setosa.SepalWidthCm), y0=min(setosa.SepalLengthCm),
    #               x1=max(setosa.SepalWidthCm), y1=max(setosa.SepalLengthCm),
    #               opacity=0.2,
    #               fillcolor="rgb(154, 79, 219)",
    #               line_color="rgb(154, 79, 219)",
    #               )
    #
    # fig1.add_shape(type="circle",
    #               xref="x", yref="y",
    #               x0=min(versicolor.SepalWidthCm), y0=min(versicolor.SepalLengthCm),
    #               x1=max(versicolor.SepalWidthCm), y1=max(versicolor.SepalLengthCm),
    #               opacity=0.2,
    #               fillcolor="rgb(79, 196, 219)",
    #               line_color="rgb(79, 196, 219)",
    #               )
    #
    # fig1.add_shape(type="circle",
    #                xref="x", yref="y",
    #                x0=min(virginica.SepalWidthCm), y0=min(virginica.SepalLengthCm),
    #                x1=max(virginica.SepalWidthCm), y1=max(virginica.SepalLengthCm),
    #                opacity=0.2,
    #                fillcolor="rgb(225, 69, 69)",
    #                line_color="rgb(225, 69, 69)",
    #                )

    # customizing figure
    fig1.update_traces(mode='markers', marker_line_width=1.5, marker_size=12)
    fig1.update_layout(template='plotly_white', xaxis=dict(title_text='SepalWidthCm', title_standoff=10),
                       yaxis=dict(title_text='SepalLengthCm', title_standoff=10),
                       title_text='Sepal Length/Width', title_x=0.5)
    fig1.update_xaxes(showline=True, linewidth=3, linecolor='black',
                      showspikes=True, spikecolor='red', spikethickness=2)
    fig1.update_yaxes(showline=True, linewidth=3, linecolor='black',
                      showspikes=True, spikecolor='red', spikethickness=2)
    return fig1


iris_scatterplot = iris_scatter(iris)
