from src.database.models import ReservaDB


def test_crear_reserva_exitosa_y_persiste_en_bd(client_con_bd, db_session):

    payload = {
        "cliente_email": "test@correo.com",
        "zona": "VIP",
        "cantidad": 2,
    }


    response = client_con_bd.post("/reservas/concierto-2026", json=payload)

    assert response.status_code == 201, (
        f"Se esperaba 201 Created, se obtuvo {response.status_code}. "
        f"Body: {response.text}"
    )

    reserva_en_bd = (
        db_session.query(ReservaDB)
        .filter(ReservaDB.evento_id == "concierto-2026")
        .first()
    )

    assert reserva_en_bd is not None, "No se encontró ningún registro en la BD para concierto-2026"
    assert reserva_en_bd.cliente_email == "test@correo.com", (
        f"Email esperado: test@correo.com — Email encontrado: {reserva_en_bd.cliente_email}"
    )