
//Codigo para sensor de temperatura, humedad y luminosidad

// #include <dht.h>
// dht DHT;

// #define DHT22_PIN 2 
// #define IN A0
    
float hum;  
float temp; 
float lux;

void setup(){
    Serial.begin(9600);
}

void loop(){
//    int chk = DHT.read22(DHT22_PIN);
//    int lux = map(analogRead(IN), 1023, 0, 0, 100);

//    hum = DHT.humidity;
//    temp= DHT.temperature;

// Creo un numero random entre 60 y 80 para emular la humedad 
// Creo un numero random entre 24 y 28 para emular los grados de la temperatura
// Creo un numero random entre 1500 y 3000 para emular la luminosidad 
// Tomo valores cada segundo, para mi es suficiente un dato por segundo
    
    hum = random(60, 80);
    temp = random(24, 28);
    lux = random(1500, 3000);
    
    Serial.print((String)"Humidity: " + hum + (String)" %, ");
    Serial.print((String)"Temp: " + temp + (String)" C, ");
    Serial.println((String)"Lux: " + lux + (String)" %");
    delay(1000); 
}
