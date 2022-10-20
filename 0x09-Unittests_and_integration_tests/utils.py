#!/usr/bin/env python3
"""Utilidades genéricas para el cliente de github org.
"""
solicitudes de importación
desde functools importar envolturas
de escribir importar (
    Cartografía,
    Secuencia,
    Ningún,
    dictado,
    llamable,
)

__todo__ = [
    "access_nested_map",
    "get_json",
    "memorizar",
]


def access_nested_map(nested_map: Mapeo, ruta: Secuencia) -> Cualquiera:
    """Acceda al mapa anidado con la ruta clave.
    Parámetros
    ----------
    nested_map: Mapeo
        Un mapa anidado
    camino: Secuencia
        una secuencia de clave que representa una ruta al valor
    Ejemplo
    -------
    >>> mapa_anidado = {"a": {"b": {"c": 1}}}
    >>> acceso_mapa_anidado(mapa_anidado, ["a", "b", "c"])
    1
    """
    para clave en la ruta:
        si no es una instancia (mapa_anidado, Mapeo):
            aumentar KeyError (clave)
        mapa_anidado = mapa_anidado[clave]

    devolver mapa_anidado


def get_json (url: str) -> dictado:
    """Obtener JSON desde una URL remota.
    """
    respuesta = solicitudes.get(url)
    devolver respuesta.json()


def memoize(fn: Invocable) -> Invocable:
    """Decorador para memorizar un método.
    Ejemplo
    -------
    clase MiClase:
        @memoizar
        def a_method(auto):
            print("un_método llamado")
            volver 42
    >>> mi_objeto = MiClase()
    >>> mi_objeto.un_método
    un_método llamado
    42
    >>> mi_objeto.un_método
    42
    """
    nombre_atributo = "_{}".formato(fn.__nombre__)

    @envolturas(fn)
    def memorizado(auto):
        """"envolturas memorizadas"""
        si no hasattr(self, attr_name):
            setattr(self, nombre_atributo, fn(self))
        devuelve getattr(self, nombre_atributo)

    devolver propiedad (memorizada)
