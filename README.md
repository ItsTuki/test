# test

Repositorio de pruebas con funciones auxiliares en Python pensadas para un bot de Discord (ver [Bot-Discord](https://github.com/ItsTuki/Bot-Discord)).

## Funciones de `bot_logic.py`

| Función | Qué hace |
|---|---|
| `gen_pass(largo)` | Devuelve una contraseña aleatoria con letras, números y símbolos. |
| `flip_coin()` | Lanza una moneda y devuelve `"Cara"` o `"Cruz"`. |
| `comands()` | Devuelve el texto de ayuda con la lista de comandos del bot. |

## Uso

```python
from bot_logic import gen_pass, flip_coin

print(gen_pass(10))
print(flip_coin())
```
