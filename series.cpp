#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    const long long n_max = 1000000; // 10^6 términos
    const int puntos_muestra = 1000; // Puntos para el archivo
    
    ofstream archivo("datos_series.csv");
    
    // Encabezado del CSV
    archivo << "n,Serie_Armonica,Serie_Inversos_Cuadrados" << endl;
    
    double suma_armonica = 0.0;
    double suma_cuadrados = 0.0;
    
    // Calcular el paso logarítmico para el muestreo
    double paso_log = pow(10, log10(n_max) / (puntos_muestra - 1));
    long long siguiente_punto = 1;
    
    cout << "Calculando series hasta n = " << n_max << "..." << endl;
    
    for (long long n = 1; n <= n_max; n++) {
        suma_armonica += 1.0 / n;
        suma_cuadrados += 1.0 / (n * n);
        
        // Guardar datos en puntos específicos (escala logarítmica)
        if (n >= siguiente_punto || n == n_max) {
            archivo << n << "," << fixed << setprecision(10) 
                    << suma_armonica << "," << suma_cuadrados << endl;
            
            // Calcular el siguiente punto de muestreo
            siguiente_punto = static_cast<long long>(siguiente_punto * paso_log);
            if (siguiente_punto <= n) siguiente_punto = n + 1;
            
            // Mostrar progreso en consola
            if (n % 100000 == 0) {
                cout << "Procesado: " << n << "/" << n_max << " terminos" << endl;
            }
        }
    }
    
    archivo.close();
    
    cout << "¡Calculo completado!" << endl;
    cout << "Resultados guardados en 'datos_series.csv'" << endl;
    cout << "Valor final serie armonica: " << suma_armonica << endl;
    cout << "Valor final serie inversos cuadrados: " << suma_cuadrados << endl;
    cout << "Valor teorico pi cuadrada/6: " << M_PI*M_PI/6.0 << endl;
    
    return 0;
}