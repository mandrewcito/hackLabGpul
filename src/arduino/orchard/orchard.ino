#include "DHT.h"

#define DHTPIN 2     // what digital pin we're connected to

#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

long distancia;
long tiempo;

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(9, OUTPUT); /*activación del pin 9 como salida: para el pulso ultrasónico*/
  pinMode(8, INPUT);

  
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

   digitalWrite(9,LOW); /* Por cuestión de estabilización del sensor*/
   delayMicroseconds(5);
   digitalWrite(9, HIGH); /* envío del pulso ultrasónico*/
   delayMicroseconds(10);
   tiempo=pulseIn(8, HIGH); /* Función para medir la longitud del pulso entrante. Mide el tiempo que transcurrido entre el envío
   del pulso ultrasónico y cuando el sensor recibe el rebote, es decir: desde que el pin 12 empieza a recibir el rebote, HIGH, hasta que    deja de hacerlo, LOW, la longitud del pulso entrante*/
   distancia= int(0.017*tiempo); /*fórmula para calcular la distancia obteniendo un valor entero*
   /*Monitorización en centímetros por el monitor serial*/
  // Serial.println(distancia);


  float t = dht.readTemperature();
  float h = dht.readHumidity();
  
  Serial.print(t);
  Serial.print(",");
  Serial.print(h);
  Serial.print(",");
  Serial.print(666);
  Serial.print(",");
  Serial.print(0.01);
  Serial.print(",");
  Serial.println(distancia);
}
