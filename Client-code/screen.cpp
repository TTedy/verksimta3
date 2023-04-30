#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <chrono>
#include <thread>
#include <mosquitto.h>
#include "led-matrix.h"
#include "graphics.h"

using namespace rgb_matrix;

volatile bool interrupt_received = false;

// Handle CTRL-C and quit
static void InterruptHandler(int signo) {
  interrupt_received = true;
}

// MQTT message callback
void mqtt_callback(struct mosquitto *mosq, void *userdata, const struct mosquitto_message *message) {
  // Toggle the checkmark when a message is received
  bool *checked = static_cast<bool*>(userdata);
  *checked = !(*checked);
}

int main(int argc, char **argv) {
  // Initialize the LED matrix
  RGBMatrix::Options options;
  options.rows = 32;
  options.cols = 64;
  options.chain_length = 2;
  options.parallel = 1;
  options.row_address_type = 0;
  options.multiplexing = 0;
  options.disable_hardware_pulsing = false;
  options.brightness = 100;
  options.pwm_lsb_nanoseconds = 130;
  options.scan_mode = static_cast<ScanMode>(0);
  options.pixel_mapper_config = "U-mapper";
  RGBMatrix *matrix = CreateMatrixFromFlags(&argc, &argv, &options);
  if (matrix == nullptr) {
    return 1;
  }

  // Initialize the MQTT client
  mosquitto_lib_init();
  struct mosquitto *mosq = mosquitto_new(NULL, true, NULL);
  if (mosq == nullptr) {
    return 1;
  }
  bool checked = false;
  mosquitto_userdata_set(mosq, &checked);
  mosquitto_message_callback_set(mosq, mqtt_callback);
  mosquitto_connect(mosq, "localhost", 1883, 60);
  mosquitto_subscribe(mosq, NULL, "checkmark", 0);

  // Load the initial image
  const char* image_path = "uno_cards/g3.png";
  Matrix* image = matrix->CreateMatrixFromImage(image_path);
  if (image == nullptr) {
    matrix->Clear();
    delete matrix;
    return 1;
  }

  // Main loop
  signal(SIGTERM, InterruptHandler);
  signal(SIGINT, InterruptHandler);
  while (!interrupt_received) {
    // Draw the image
    matrix->Clear();
    matrix->DrawImage(image, 0, 0);

    // Draw the checkmark if checked
    if (checked) {
      for (int x = 48; x < 64; ++x) {
        for (int y = 0; y < 16; ++y) {
          matrix->SetPixel(x, y, 0, 255, 0);
        }
      }
    }

    // Update the display
    matrix->SwapOnVSync();
    std::this_thread::sleep_for(std::chrono::milliseconds(50));

    // Check for new images
    if (mosquitto_loop(mosq, 0, 1) != MOSQ_ERR_SUCCESS) {
      break;
    }
    const char* new_image_path = nullptr;
    if (checked) {
      new_image_path = "uno_cards/g5.png";
    } else {
      new_image_path = "uno_cards


/* 
g++ mqtt_led_matrix.cpp -o mqtt_led_matrix -lmosquitto -lrgbmatrix
sudo ./mqtt_led_matrix

sudo apt-get update
sudo apt-get install libmosquitto-dev librgbmatrix-dev

sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D 1 --led-rows=16 --led-cols=32 --led-brightness=50 --led-scan-mode=0 --led-pixel-mapper="Rotate:90" /home/pi/image.png
*/

