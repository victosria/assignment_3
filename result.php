<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Recupera valores do form (validação básica)
    $x = isset($_POST['x']) ? floatval($_POST['x']) : 0;
    $y = isset($_POST['y']) ? floatval($_POST['y']) : 0;
    $z = isset($_POST['z']) ? floatval($_POST['z']) : 0;
    
    if ($x === '' || $y === '' || $z === '') {
        die("Error: Please enter valid numbers for x, y, z.");
    }
    
    // Chama o script Python com argumentos (passa como string para exec)
    $command = "python3 process_input.py " . $x . " " . $y . " " . $z;
    $output = shell_exec($command . " 2>&1");  // Captura output e erros
    
    // Exibe o output do Python (que é HTML)
    echo $output;
} else {
    // Se não for POST, redireciona para form
    header("Location: index.php");
    exit();
}
?>