import numpy as np
import pandas as pd
from fpdf import FPDF


def calculate_pearson_correlation(X, Y):
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    std_X = np.std(X)
    std_Y = np.std(Y)
    correlation_coefficient = np.mean((X - mean_X) * (Y - mean_Y)) / (std_X * std_Y)
    return correlation_coefficient

def calculate_correlation_matrix(data):
    num_features = data.shape[1]
    correlation_matrix = np.zeros((num_features, num_features))

    for i in range(num_features):
        for j in range(num_features):
            correlation_matrix[i, j] = calculate_pearson_correlation(data.iloc[:, i], data.iloc[:, j])
    return correlation_matrix

def correlation_matrix(data,columns):
    correlation_matrix = calculate_correlation_matrix(data)
    frame_with_columns = pd.DataFrame(correlation_matrix, columns=columns, index=columns)
    print("Correlation Matrix:")
    print(frame_with_columns)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Correlation Matrix", ln=True, align="C")
    pdf.set_font("Arial", size=10)
    cell_width = 37
    cell_height = 10

    for key,col in enumerate(frame_with_columns.columns):
        if(key == 0):
            pdf.cell(cell_width, cell_height, '', border=1)
        pdf.cell(cell_width, cell_height, col, border=1)
    pdf.ln()

    for index, row in frame_with_columns.iterrows():
        pdf.cell(cell_width, cell_height, str(index), border=1)
        for value in row:
            pdf.cell(cell_width, cell_height, str(round(value,6)), border=1)
        pdf.ln()
    pdf.output("correlation_matrix.pdf")
    return frame_with_columns


def highest_correlation(matrix,columns):
    num_features = len(columns)
    corr_values = []
    for i in range(num_features):
        for j in range(i + 1, num_features):
            corr_values.append((columns[i], columns[j], abs(matrix.iloc[i, j])))

    sorted_corr_values = sorted(corr_values, key=lambda x: x[2], reverse=True)
    top_2_corr_values = sorted_corr_values[:2]

    print("Top 2 Highest Correlations:")
    for pair in top_2_corr_values:
        print(pair[0], "-", pair[1], ":", matrix.loc[pair[0], pair[1]])

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Highest Correlation", ln=True, align="C")
    pdf.set_font("Arial", size=10)

    pdf.cell(200, 10, txt="Top 2 Highest Correlations", ln=True, align="C")
    pdf.cell(200, 10, txt="", ln=True)

    for pair in top_2_corr_values:
        pdf.cell(200, 10, txt=f"{pair[0]} - {pair[1]} : {matrix.loc[pair[0], pair[1]]}", ln=True)
    pdf.output("highest_correlation.pdf")

data = pd.read_csv('network_data.csv', header=None)
columns = ['Packet Size', 'Payload', 'Request Duration', 'Destination Port']
matrix = correlation_matrix(data,columns)
highest_correlation(matrix,columns)
