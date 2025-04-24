#4. Decorator
#Permite agregar funcionalidades o modifica funcionalidad de forma dinámica a un objeto sin modificar su estructura
class Text:
    def __init__(this,text):
        this.text = text

    def render(this) -> str:
        return this.text
    
#decorador base:
class BaseDecorator:
    def __init__(this, component):
        this._component = component

    def render(this):
        return this._component.render()
    
#decoradores concretos
class BoldDecorator(BaseDecorator):    
    def render(this):
        return f"<b>{super().render()}</b>"

class ItalicDecorator(BaseDecorator):
    def render(this):
        return f"<i>{super().render()}</i>"

class UnderlineDecorator(BaseDecorator):
    def render(this):
        return f"<u>{super().render()}</u>"
    
#Uso:
texto = Text("Lenguajes de Programación 2025A")
decorado = UnderlineDecorator(BoldDecorator(ItalicDecorator(texto)))
print(decorado.render())