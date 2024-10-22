#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <algorithm>

using namespace std;

bool leer_archivo(const string& ruta_archivo, vector<int>& numeros) {
    ifstream archivo(ruta_archivo);
    if (!archivo.is_open()) {
        cout << "Error: No se pudo abrir el archivo '" << ruta_archivo << "'." << endl;
        return false;
    }
    int numero;
    numeros.clear();
    while (archivo >> numero) {
        numeros.push_back(numero);
    }
    archivo.close();
    return !numeros.empty();
}

double ordenar_burbuja(vector<int>& numeros) {
    int n = numeros.size();
    auto start = chrono::high_resolution_clock::now();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++) {
            if (numeros[j] > numeros[j + 1]) {
                swap(numeros[j], numeros[j + 1]);
            }
        }
    }
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    return duration.count();         
}

double ordenar_conteo(vector<int>& numeros) {
    int max = *max_element(numeros.begin(), numeros.end());
    int min = *min_element(numeros.begin(), numeros.end());
    int range = max - min + 1;
    int n = numeros.size();
    vector<int> conteo(range, 0);
    vector<int> output(n);
    auto start = chrono::high_resolution_clock::now();
    for (int i = 0; i < n; i++) {
        conteo[numeros[i] - min]++;
    }

    for (int i = 1; i < conteo.size(); i++) {
        conteo[i] += conteo[i - 1];
    }

    for (int i = n - 1; i >= 0; i--) {
        output[conteo[numeros[i] - min] - 1] = numeros[i];
        conteo[numeros[i] - min]--;
    }

    for (int i = 0; i < n; i++) {
        numeros[i] = output[i];
    }

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    return duration.count();
}

void heapify(vector<int>& arr, int n, int i) {
    int largest = i; 
    int left = 2 * i + 1;  
    int right = 2 * i + 2; 
    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    if (largest != i) {
        swap(arr[i], arr[largest]); 
        heapify(arr, n, largest);
    }
}

double ordenar_heap(vector<int>& arr) {
    int n = arr.size();
    auto start = chrono::high_resolution_clock::now();
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    return duration.count();
}

double ordenar_insercion(vector<int>& arr) {
    int n = arr.size();
    auto start = chrono::high_resolution_clock::now();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    return duration.count();
}

void merge(vector<int>& a, int izq, int centro, int dere) {
    int n1 = centro - izq + 1; 
    int n2 = dere - centro;
    vector<int> izqA(n1);
    vector<int> dereA(n2);
    for (int i = 0; i < n1; i++)
        izqA[i] = a[izq + i];
    for (int j = 0; j < n2; j++)
        dereA[j] = a[centro + 1 + j];
    int i = 0, j = 0, k = izq;
    while (i < n1 && j < n2) {
        if (izqA[i] <= dereA[j]) {
            a[k] = izqA[i];
            i++;
        } else {
            a[k] = dereA[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        a[k] = izqA[i];
        i++;
        k++;
    }
    while (j < n2) {
        a[k] = dereA[j];
        j++;
        k++;
    }
}

void mergeSort(vector<int>& a, int izq, int dere);
double ordenar_merge(vector<int>& a) {
    auto start = chrono::high_resolution_clock::now();
    mergeSort(a, 0, a.size() - 1);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    return duration.count();
}

void mergeSort(vector<int>& a, int izq, int dere) {
    if (izq < dere) {
        int centro = izq + (dere - izq) / 2;
        mergeSort(a, izq, centro);
        mergeSort(a, centro + 1, dere);
        merge(a, izq, centro, dere);
    }
}

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high]; 
    int i = (low - 1); 
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}
void quickSort(vector<int>& arr, int low, int high);
double ordenar_quick(vector<int>& arr) {
    auto start = chrono::high_resolution_clock::now();
    int n = arr.size();
    quickSort(arr, 0, n - 1);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    return duration.count();
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
double ordenar_seleccion(vector<int>& arr) {
    int n = arr.size();
    auto start = chrono::high_resolution_clock::now();
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    return duration.count();
}
int main() {
    string ruta_archivo;
    vector<int> numeros;
    vector<double> tiempos_burbuja;
    vector<double> tiempos_conteo;
    vector<double> tiempos_heap;
    vector<double> tiempos_insercion;
    vector<double> tiempos_merge;
    vector<double> tiempos_quick;
    vector<double> tiempos_seleccion;
    char continuar;
    do {
        cout << "Ingrese la ruta completa del archivo (ej: C:/ruta_completa/numeros_aleatorios.txt): ";
        cin >> ruta_archivo;
        if (leer_archivo(ruta_archivo, numeros)) {
            vector<int> numeros_burbuja = numeros; 
            vector<int> numeros_conteo = numeros; 
            vector<int> numeros_heap = numeros; 
            vector<int> numeros_insercion = numeros; 
            vector<int> numeros_merge = numeros; 
            vector<int> numeros_quick = numeros; 
            vector<int> numeros_seleccion = numeros; 
            double tiempo_burbuja = ordenar_burbuja(numeros_burbuja);
            tiempos_burbuja.push_back(tiempo_burbuja);
            double tiempo_conteo = ordenar_conteo(numeros_conteo);
            tiempos_conteo.push_back(tiempo_conteo);
            double tiempo_heap = ordenar_heap(numeros_heap);
            tiempos_heap.push_back(tiempo_heap);
            double tiempo_insercion = ordenar_insercion(numeros_insercion);
            tiempos_insercion.push_back(tiempo_insercion);
            double tiempo_merge = ordenar_merge(numeros_merge);
            tiempos_merge.push_back(tiempo_merge);
            double tiempo_quick = ordenar_quick(numeros_quick);
            tiempos_quick.push_back(tiempo_quick);
            double tiempo_seleccion = ordenar_seleccion(numeros_seleccion);
            tiempos_seleccion.push_back(tiempo_seleccion);
            cout << "Desea continuar con otro archivo? (s/n): ";
            cin >> continuar;
        } else {
            cout << "No se pudo leer el archivo. Intente de nuevo." << endl;
            continuar = 's'; 
        }
    } while (continuar == 's' || continuar == 'S');

    cout << "Tiempos de ejecucion de cada algoritmo:" << endl;
    for (size_t i = 0; i < tiempos_burbuja.size(); i++) {
        cout << "Ordenamiento Burbuja " << i + 1 << ": " << tiempos_burbuja[i] << " segundos." << endl;
    }
    for (size_t i = 0; i < tiempos_conteo.size(); i++) {
        cout << "Ordenamiento Conteo " << i + 1 << ": " << tiempos_conteo[i] << " segundos." << endl;
    }
    for (size_t i = 0; i < tiempos_heap.size(); i++) {
        cout << "Ordenamiento Heap " << i + 1 << ": " << tiempos_heap[i] << " segundos." << endl;
    }
    for (size_t i = 0; i < tiempos_insercion.size(); i++) {
        cout << "Ordenamiento Insercion " << i + 1 << ": " << tiempos_insercion[i] << " segundos." << endl;
    }
    for (size_t i = 0; i < tiempos_merge.size(); i++) {
        cout << "Ordenamiento Merge " << i + 1 << ": " << tiempos_merge[i] << " segundos." << endl;
    }
    for (size_t i = 0; i < tiempos_quick.size(); i++) {
        cout << "Ordenamiento Quick " << i + 1 << ": " << tiempos_quick[i] << " segundos." << endl;
    }
    for (size_t i = 0; i < tiempos_seleccion.size(); i++) {
        cout << "Ordenamiento Seleccion " << i + 1 << ": " << tiempos_seleccion[i] << " segundos." << endl;
    }
    return 0;
}

