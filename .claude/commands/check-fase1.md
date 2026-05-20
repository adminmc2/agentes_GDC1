---
description: Valida las 10 unidades de fase 1 (U0-U9) en bucle y reporta el estado de cada una. Útil para confirmar que la estructura sigue intacta tras ediciones.
---

Ejecuta el validador de inventario para cada unidad U0-U9 y devuelve el resultado.

```bash
for u in 0 1 2 3 4 5 6 7 8 9; do
  echo -n "U$u: "
  python3 scripts/validar_inventario.py $u 2>&1 | tail -1
done
```

Si todas dan `✅ JSON válido · 0 avisos · 0 legacy`, la fase 1 sigue cerrada en su parte mecanizable. Si alguna falla, investigar inmediatamente:
- `❌ §5.10 A`: fuente declarada sin aparición literal del item → revisar fuentes del item.
- `❌ §5.11`: flexiones no unificadas → aplicar notación barra `lema/-a`.
- Otros errores: consultar `fases/1-extraccion-inventario/schema-inventario.md`.

Estado esperado (cierre v10.164): **10/10 unidades en 0/0/0**.