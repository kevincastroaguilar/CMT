
#include <dht.h>
dht DHT;

#define DHT22_PIN 2 

    
float hum;  
float temp; 
float lux=0.00,ADC_value=0.0048828125,LDR_value;

void setup(){
  pinMode(A0,INPUT);
    Serial.begin(9600);
}

void loop(){
    int chk = DHT.read22(DHT22_PIN);
    
    hum = DHT.humidity;
    temp= DHT.temperature;
    
    LDR_value=analogRead(A0);
     lux=(250.000000/(ADC_value*LDR_value))-50.000000;
    
    Serial.print("%, Humidity: ");
    Serial.print(hum);
    
    Serial.print(" Temp: ");
    Serial.print(temp);
    Serial.print(" Celcius ");
    
  Serial.println(lux);
  Serial.print(" lux ");
  
    delay(2000); 
}
