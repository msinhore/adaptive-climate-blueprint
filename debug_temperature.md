# Debug da Lógica de Temperatura

Vamos analisar um caso específico:

## Configuração:
- max_comfort_temp_val = 27°C
- outdoor_temp = 30°C (exemplo)
- comfort_category = "II" (±3°C)
- indoor_temp = 29°C (muito quente)

## Cálculos:
1. adaptive_comfort_temp = 18.9 + 0.255 × 30 = 26.55°C ≈ 26.6°C
2. comfort_tolerance = 3.0°C
3. comfort_temp_max = min(26.6 + 3.0, 27.0) = min(29.6, 27.0) = 27.0°C ✅

## Problema Identificado:
Na lógica target_temp original, quando indoor_temp > comfort_temp_max:
- Modo ocupado: comfort_temp_max = 27°C ✅
- Modo não ocupado: comfort_temp_max + setback = 27 + 2 = 29°C ❌

O problema era que quando o ambiente não estava ocupado e estava muito quente, 
a automação estava AUMENTANDO a temperatura em vez de manter o limite máximo.

## Correção Implementada:
A nova lógica para modo não ocupado:
- Se indoor_temp > comfort_temp_max: usar comfort_temp_max (nunca exceder o limite)
- Se indoor_temp < comfort_temp_min: usar comfort_temp_min - setback (com limite mínimo)
- Senão: usar adaptive_comfort_temp

Agora NUNCA ultrapassará os limites de conforto configurados pelo usuário!
