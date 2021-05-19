import i2cdriver


def main(port: str):
    i2c = i2cdriver.I2CDriver("/dev/ttyUSB0")
    i2c.scan()


if __name__ == '__main__':
    main("/dev/ttyUSB0")
