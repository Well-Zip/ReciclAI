#include <Servo.h>

Servo meuServo;  // Criar um objeto servo

void setup() {
    meuServo.attach(9);  // Pino 9 (Arduino)
    Serial.begin(9600);  // Inicializar comunicação serial
}

void loop() {
    // Variável para armazenar o tempo em que o último comando 'A' foi recebido
    static unsigned long tempoUltimoComandoA = 0;
    
    // Variável para rastrear se a porta está aberta
    static bool is_open = false;

    // Lendo o caracter enviado pela serial
    char comando = Serial.read();
    
    if (comando == 'A') {
        // Atualiza o tempo em que o comando 'A' foi recebido
        tempoUltimoComandoA = millis();
        
        // Verifica se a porta já está aberta
        if (!is_open) {
            // Abre a porta se ainda não estiver aberta
            meuServo.write(0);     // Abre a porta
            delay(170);           // Tempo que o servo será alimentado
            meuServo.write(90);  // Posiciona o servo no centro
            is_open = true;     // Atualiza o estado da porta para aberta
        }
    }
    
    // Verifica se passaram mais de 4 segundos desde o último comando 'A' e se a porta está aberta
    if (is_open && millis() - tempoUltimoComandoA >= 4000) {
        // Fecha a porta automaticamente
        meuServo.write(180);        // Fecha a porta
        delay(135);                // Tempo que o servo será alimentado
        meuServo.write(90);       // Posiciona o servo no centro
        is_open = false;         // Atualiza o estado da porta para fechada
    }
}
