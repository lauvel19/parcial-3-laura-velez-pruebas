import httpx


BASE_URL = "http://localhost:8001"

PRECIO_GENERAL = 50_000 


def test_flujo_completo_calculo_total_recaudado():

    evento_id = "sistema-evento-xyz"
    zona = "General"
    cantidad = 3
    total_esperado = cantidad * PRECIO_GENERAL 

    # Paso 1: crear reserva 
    response_post = httpx.post(
        f"{BASE_URL}/reservas/{evento_id}",
        json={
            "cliente_email": "sistema@test.com",
            "zona": zona,
            "cantidad": cantidad,
        },
    )
    assert response_post.status_code == 201, (
        f"POST falló con {response_post.status_code}: {response_post.text}"
    )

    # Paso 2: obtener resumen 
    response_get = httpx.get(f"{BASE_URL}/reservas/{evento_id}/resumen")
    assert response_get.status_code == 200, (
        f"GET resumen falló con {response_get.status_code}: {response_get.text}"
    )

    # Paso 3: validar cálculo de negocio
    data = response_get.json()
    assert data["total_recaudado"] == total_esperado, (
        f"Total esperado: {total_esperado} COP — "
        f"Total recibido: {data['total_recaudado']} COP"
    )