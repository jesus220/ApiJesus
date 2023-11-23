
import pytest
from api.models import General
# Create your tests here.


def test_crear_instancia():
        instancia = General.objects.create_user(
            Id_genera='A'
            precios='precio1',
            empanadas='empanada1',
            cortes='corte1',
            guarniciones='guarnicion1',
            postres='postre1',
            salsapastas='salsapasta1',
            alcohol='alcohol1',
            cervezas='cerveza1',
            refrescos='refresco1',
            cafes='cafe1'
        )

        # Verifica cada campo individualmente 
        assert test_crear_instancia.Id_gener == 'B'
        assert test_crear_instancia.precios == 'precio1'
        