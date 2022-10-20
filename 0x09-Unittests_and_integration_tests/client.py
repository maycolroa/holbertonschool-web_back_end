#!/usr/bin/env python3
"""Un cliente de organización de github
"""
de escribir importar (
    Lista,
    dictado,
)

de la importación de utilidades (
    obtener_json,
    acceso_mapa_anidado,
    memorizar,
)


clase GithubOrgClient:
    """Un cliente de organización de Githib
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> Ninguno:
        """Método de inicio de GithubOrgClient"""
        self._org_name = org_name

    @memoizar
    def org(self) -> dictado:
        """Memorizar organización"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @propiedad
    def _public_repos_url(self) -> str:
        """URL pública de repositorios"""
        volver self.org["repos_url"]

    @memoizar
    def repos_payload(self) -> dictado:
        """Memorizar carga útil de repositorios"""
        devolver get_json(self._public_repos_url)

    def public_repos(self, licencia: str = Ninguno) -> List[str]:
        """Repos públicos"""
        json_payload = self.repos_payload
        public_repos = [
            repositorio ["nombre"] para repositorio en json_payload
            si la licencia es Ninguna o self.has_license(repo, license)
        ]

        volver public_repos

    @métodoestático
    def tiene_licencia(repo: Dict[str, Dict], clave_licencia: str) -> bool:
        """Estático: tiene_licencia"""
        afirmar clave_licencia no es Ninguno, "clave_licencia no puede ser Ninguno"
        probar:
            has_license = access_nested_map(repo, ("licencia", "clave")) == clave_licencia
        excepto KeyError:
            falso retorno
        volver has_license
