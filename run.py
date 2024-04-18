# run.py

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Definir la tasa de interés como una constante global
TASA_INTERES = 0.1  # 10%

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    if request.method == 'POST':
        valor_auto_str = request.form['valor_auto']
        # Eliminar las comas de la cadena
        valor_auto_str = valor_auto_str.replace(',', '')
        valor_auto = float(valor_auto_str)
        entrega_inicial = calcular_entrega_inicial(valor_auto)
        monto_cuota_12, monto_cuota_24, monto_cuota_36 = calcular_monto_cuotas(valor_auto, entrega_inicial)
        return render_template('resultado.html', valor_auto=valor_auto, entrega_inicial=entrega_inicial, monto_cuota_12=monto_cuota_12, monto_cuota_24=monto_cuota_24, monto_cuota_36=monto_cuota_36, tasa_interes=TASA_INTERES)
    else:
        return render_template('resultado.html')

def calcular_monto_cuotas(valor_auto, entrega_inicial):
    monto_financiado = valor_auto - entrega_inicial
    # Calcular la cuota para 12 meses
    monto_cuota_12 = calcular_cuota(monto_financiado, 12)
    # Calcular la cuota para 24 meses
    monto_cuota_24 = calcular_cuota(monto_financiado, 24)
    # Calcular la cuota para 36 meses
    monto_cuota_36 = calcular_cuota(monto_financiado, 36)
    return round(monto_cuota_12, 2), round(monto_cuota_24, 2), round(monto_cuota_36, 2)

def calcular_cuota(monto_financiado, cuotas):
    # Fórmula para calcular la cuota mensual con interés compuesto
    tasa_mensual = TASA_INTERES / 12
    cuota = monto_financiado * (tasa_mensual) / (1 - (1 + tasa_mensual) ** (-cuotas))
    return cuota

def calcular_entrega_inicial(valor_auto):
    entrega_inicial = valor_auto * 0.6  # El 60% del valor del auto
    return entrega_inicial

if __name__ == '__main__':
    app.run(debug=True)
