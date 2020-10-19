
byte buttons[] = {3,2}; // pin numbers of the buttons that we'll use
#define NUMBUTTONS sizeof(buttons)
int buttonState[NUMBUTTONS];
int lastButtonState[NUMBUTTONS];
boolean buttonIsPressed[NUMBUTTONS];
boolean on = false;

long lastDebounceTime = 0; // the last time the output pin was toggled
long debounceDelay = 25; // the debounce time; increase if the output flickers

void setup() {
  Serial.begin(9600);
  // define pins:
  for (int i=0; i<(NUMBUTTONS-1); i++) {
    pinMode(buttons[i], INPUT);
    lastButtonState[i]=HIGH;
    buttonIsPressed[i]=false;
  }
  Serial.println("startup");
}

void loop()
{
  check_buttons();
  action();
}

void check_buttons() {
  for (int currentButton=0; currentButton<NUMBUTTONS; currentButton++) {
    int reading = digitalRead(buttons[currentButton]);
    if (reading != lastButtonState[currentButton]) { lastDebounceTime = millis(); }
    if ((millis() - lastDebounceTime) > debounceDelay) {
      if (reading != buttonState[currentButton]) {
        buttonState[currentButton] = reading;
        if (buttonState[currentButton]==LOW) {
          buttonIsPressed[currentButton]=true;
        }
      }
    }
    // save the reading.  Next time through the loop, it'll be the lastButtonState:
    lastButtonState[currentButton] = reading;
  }
}

void action() {
  for (int currentButton=0; currentButton<NUMBUTTONS; currentButton++) {
    if (buttonIsPressed[currentButton]) {
      Serial.print("button "); Serial.println(buttons[currentButton]);
      if (buttons[currentButton]==3) { // -------- Button 3 controls action A
        // do action A stuff here
      } else if (buttons[currentButton]== 2) { // -------- Button 5 controls action C
        // do action C stuff here
      }
      buttonIsPressed[currentButton]=false; //reset the button
    }
  }

}
