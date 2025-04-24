#6. Command
# Encapsula una petición de una funcionalidad como un objeto, permitiendo parametrizar
# las solicitudes de acuerdo a los clientes, y manejar peticiones como objetos (historia, cola de peticiones, etc)

# Receptor del comando:
class Light:

    def on(this):
        print("Light is on")

    def off(this):
        print("Light is off")

#Comando base:
class Command:
    def exec_command(this):
        pass

#Comandos concretos:
class TurnLightOn(Command):
    # cada comando concreto se instancia determinando también qué objeto recibe el comando
    # y la operación a ejecutar
    def __init__(this, light:Light):
        this._light = light

    def exec_command(this):
        this._light.on()

class TurnLightOff(Command):
    def __init__(this, light:Light):
        this._light = light

    def exec_command(this):
        this._light.off()

#Invocador:
class LightRemoteControl:

    def __init__(this):
        this._command = None

    def setCommand(this, command: Command):
        this._command = command

    def pushButton(this):
        this._command.exec_command()

#Uso:
bedroomLight = Light()
turnOn = TurnLightOn(bedroomLight)
turnOff = TurnLightOff(bedroomLight)

remoteControl = LightRemoteControl()
remoteControl.setCommand(turnOn)
remoteControl.pushButton()

remoteControl.setCommand(turnOff)
remoteControl.pushButton()