package orden;
import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.*;

public class Practica_honorio {
    public static void main(String[] args) {
        String folderPath = "C:\\Users\\Usuario\\Desktop\\python\\ADA_DATOS-main";
        String outputFile = "resultados_java.csv";
        Map<String, Double> results = new HashMap<>();

        File folder = new File(folderPath);
        File[] files = folder.listFiles((dir, name) -> name.endsWith(".txt"));

        if (files != null) {
            for (File file : files) {
                List<Integer> numbers = readNumbersFromFile(file.getPath());
                System.out.println("Processing file: " + file.getName());

                for (String algorithm : Arrays.asList("Bubble Sort", "Counting Sort", "Heap Sort", 
                                                      "Insertion Sort", "Merge Sort", "Quick Sort", 
                                                      "Selection Sort")) {
                    long duration = measureSortTime(numbers, algorithm);
                    results.put(file.getName() + " - " + algorithm, duration / 1_000_000_000.0); // Convert to seconds
                }
            }
        }

        saveResultsToCSV(results, outputFile);
        printAggregatedResults(results);
    }

    private static List<Integer> readNumbersFromFile(String filePath) {
        try {
            String content = new String(Files.readAllBytes(Paths.get(filePath)));
            return Arrays.stream(content.split("\\s+")) 
                         .map(s -> s.replaceAll("[,\\[\\]]", "").trim()) 
                         .filter(s -> !s.isEmpty()) 
                         .map(Integer::parseInt) 
                         .collect(Collectors.toList());
        } catch (IOException | NumberFormatException e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    private static long measureSortTime(List<Integer> arr, String algorithm) {
        List<Integer> copy = new ArrayList<>(arr);
        long startTime = System.nanoTime();
        
        switch (algorithm) {
            case "Bubble Sort":
                bubbleSort(copy);
                break;
            case "Counting Sort":
                countingSort(copy);
                break;
            case "Heap Sort":
                heapSort(copy);
                break;
            case "Insertion Sort":
                insertionSort(copy);
                break;
            case "Merge Sort":
                mergeSort(copy);
                break;
            case "Quick Sort":
                quickSort(copy);
                break;
            case "Selection Sort":
                selectionSort(copy);
                break;
        }

        return System.nanoTime() - startTime;
    }

    private static void saveResultsToCSV(Map<String, Double> results, String outputFile) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
            writer.write("Archivo,Duracion (s)\n");
            for (Map.Entry<String, Double> entry : results.entrySet()) {
                writer.write(entry.getKey() + "," + String.format("%.6f", entry.getValue()) + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void printAggregatedResults(Map<String, Double> results) {
        Map<String, List<Double>> aggregatedResults = new HashMap<>();

        for (String key : results.keySet()) {
            String algorithm = key.split(" - ")[1];
            aggregatedResults.putIfAbsent(algorithm, new ArrayList<>());
            aggregatedResults.get(algorithm).add(results.get(key));
        }

        for (Map.Entry<String, List<Double>> entry : aggregatedResults.entrySet()) {
            Collections.sort(entry.getValue());
            List<String> formattedResults = entry.getValue().stream()
                                                   .map(val -> String.format("%.6f", val))
                                                   .collect(Collectors.toList());
            System.out.println(entry.getKey() + ": " + formattedResults);
        }
    }
    private static void bubbleSort(List<Integer> arr) {
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr.get(j) > arr.get(j + 1)) {
                    Collections.swap(arr, j, j + 1);
                }
            }
        }
    }
    private static void countingSort(List<Integer> arr) {
        if (arr.isEmpty()) return;

        int maxVal = Collections.max(arr);
        int minVal = Collections.min(arr);
        int range = maxVal - minVal + 1;
        int[] count = new int[range];
        List<Integer> output = new ArrayList<>(Collections.nCopies(arr.size(), 0));

        for (int num : arr) {
            count[num - minVal]++;
        }
        for (int i = 1; i < count.length; i++) {
            count[i] += count[i - 1];
        }
        for (int i = arr.size() - 1; i >= 0; i--) {
            output.set(count[arr.get(i) - minVal] - 1, arr.get(i));
            count[arr.get(i) - minVal]--;
        }
        for (int i = 0; i < arr.size(); i++) {
            arr.set(i, output.get(i));
        }
    }

    private static void heapSort(List<Integer> arr) {
        int n = arr.size();
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }
        for (int i = n - 1; i > 0; i--) {
            Collections.swap(arr, 0, i);
            heapify(arr, i, 0);
        }
    }

    private static void heapify(List<Integer> arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr.get(left) > arr.get(largest)) {
            largest = left;
        }
        if (right < n && arr.get(right) > arr.get(largest)) {
            largest = right;
        }
        if (largest != i) {
            Collections.swap(arr, i, largest);
            heapify(arr, n, largest);
        }
    }
    private static void insertionSort(List<Integer> arr) {
        for (int i = 1; i < arr.size(); i++) {
            int key = arr.get(i);
            int j = i - 1;
            while (j >= 0 && arr.get(j) > key) {
                arr.set(j + 1, arr.get(j));
                j--;
            }
            arr.set(j + 1, key);
        }
    }
    private static void mergeSort(List<Integer> arr) {
        if (arr.size() > 1) {
            int mid = arr.size() / 2;
            List<Integer> left = new ArrayList<>(arr.subList(0, mid));
            List<Integer> right = new ArrayList<>(arr.subList(mid, arr.size()));
            mergeSort(left);
            mergeSort(right);
            int i = 0, j = 0, k = 0;

            while (i < left.size() && j < right.size()) {
                if (left.get(i) <= right.get(j)) {
                    arr.set(k++, left.get(i++));
                } else {
                    arr.set(k++, right.get(j++));
                }
            }

            while (i < left.size()) {
                arr.set(k++, left.get(i++));
            }
            while (j < right.size()) {
                arr.set(k++, right.get(j++));
            }
        }
    }

    private static List<Integer> quickSort(List<Integer> arr) {
        if (arr.size() <= 1) {
            return arr;
        }
        int pivot = arr.get(arr.size() / 2);
        List<Integer> left = new ArrayList<>();
        List<Integer> middle = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        for (int num : arr) {
            if (num < pivot) left.add(num);
            else if (num == pivot) middle.add(num);
            else right.add(num);
        }
        List<Integer> sorted = new ArrayList<>();
        sorted.addAll(quickSort(left));
        sorted.addAll(middle);
        sorted.addAll(quickSort(right));
        return sorted;
    }

    private static void selectionSort(List<Integer> arr) {
        for (int i = 0; i < arr.size(); i++) {
            int minIdx = i;
            for (int j = i + 1; j < arr.size(); j++) {
                if (arr.get(j) < arr.get(minIdx)) {
                    minIdx = j;
                }
            }
            Collections.swap(arr, i, minIdx);
        }
    }

}
