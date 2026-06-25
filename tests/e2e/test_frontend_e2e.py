import re
import pytest
from playwright.sync_api import Page, expect

FRONTEND_URL = "http://localhost:4200/reservas"


def test_reserva_vip_muestra_total_en_resumen(page: Page):
    """
    Prueba E2E de frontend con Playwright.
    Sin sleeps manuales — usa expect() con esperas dinámicas nativas.
    
    """
    #1. Navegar
    page.goto(FRONTEND_URL)

    #2. Diligenciar formulario
    page.get_by_test_id("input-email-cliente").fill("lau@ticketfast.com")

    page.get_by_test_id("select-zona-evento").select_option("VIP")

    page.get_by_test_id("input-cantidad-asientos").fill("1")

    # 3. Confirmar reserva 
    page.get_by_test_id("btn-confirmar-reserva").click()

    # 4. Verificar resumen sin sleeps
    resumen = page.get_by_test_id("seccion-resumen-total")
    expect(resumen).to_contain_text("150.000")