#!/usr/bin/env python3
# Script para processar x, y, z via argumentos de linha de comando.
# Observação: Usa sys.argv para inputs. Trata divisão por zero. Output é HTML para display direto.

import sys

# Verifica se há 4 argumentos (script + 3 vars)
if len(sys.argv) != 4:
    print("<h1>Error: Provide x, y, z as arguments.</h1>")
    sys.exit(1)

try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = float(sys.argv[3])
    
    # Preserva original para display
    x_original = x
    
    # Operações com shortcut operators (modifica x in-place)
    x += y  # x = x + y
    step1 = f"x += y → x = {x_original} + {y} = {x}"
    
    x -= z  # x = x - z
    step2 = f"x -= z → x = {x} - {z} = {x}"  # Nota: x já é o novo valor
    
    x *= y  # x = x * y
    step3 = f"x *= y → x = {x} * {y} = {x}"
    
    x %= z  # x = x % z (modulo; assume z != 0 para % também, mas Python permite z=0 com erro)
    step4 = f"x %= z → x = {x} % {z} = {x}"
    
    # Divisão: Verifica z != 0
    if z != 0:
        x /= z  # x = x / z
        step5 = f"x /= z → x = {x} / {z} = {x}"
        division_error = False
    else:
        step5 = "Division skipped: z = 0 (cannot divide by zero)"
        division_error = True
    
    # Resultado final
    final_result = x + y + z
    final_step = f"Final Result = x + y + z = {x} + {y} + {z} = {final_result}"
    
    # Output HTML (para display direto no browser via PHP)
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Calculation Results</title>
    </head>
    <body>
        <h1>Calculation Results</h1>
        <p>Inputs: x = """ + str(x_original) + """, y = """ + str(y) + """, z = """ + str(z) + """</p>
        
        <h2>Intermediate Steps:</h2>
        <ul>
            <li>""" + step1 + """</li>
            <li>""" + step2 + """</li>
            <li>""" + step3 + """</li>
            <li>""" + step4 + """</li>
            <li>""" + step5 + """</li>
        </ul>
    """)
    if division_error:
        print('        <li style="color: red;">Warning: Division by zero avoided.</li>')
    print("""
        </ul>
        <h2>""" + final_step + """</h2>
        <a href="index.php">Back to Form</a>
    </body>
    </html>
    """)
    
except ValueError:
    print("<h1>Error: Invalid numbers provided.</h1>")
    sys.exit(1)
except ZeroDivisionError:
    print("<h1>Error: Division by zero in modulo.</h1>")
    sys.exit(1)