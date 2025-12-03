Projeto IoT – Sistema de Monitoramento para Forno de Cerâmica
Gabriella, Marcela, Maria Eduarda e Miguel Fortunato. 

Descrição do Projeto
    Este projeto IoT tem como objetivo desenvolver um sistema de monitoramento e segurança voltado para ambientes industriais de cerâmica, onde operadores trabalham próximos a fornos e chapas de alta temperatura.
    A solução emprega sensores para acompanhar temperatura, umidade e proximidade física, emitindo alertas sonoros e visuais quando condições de risco são detectadas. Dessa forma, o sistema contribui diretamente para a prevenção de acidentes, controle ambiental e melhoria da segurança operacional.

Hardware Utilizado
    A seguir estão listados os componentes empregados na montagem do sistema:
        Microcontrolador
        - Raspberry Pi Pico
            Responsável pelo processamento dos dados dos sensores e acionamento dos atuadores.
        Sensores
        - DHT22 – Sensor de temperatura e umidade
            Utilizado para monitorar o clima próximo ao forno, garantindo leitura precisa da temperatura ambiente e umidade relativa do ar.
        - HC-SR04 – Sensor ultrassônico de distância
            Detecta a aproximação de operadores ou objetos, auxiliando na identificação de situações de risco.
        Atuadores
        - Buzzer
            Emite um alerta sonoro imediato quando o sistema identifica perigo térmico ou aproximação excessiva.
        - LEDs (verde, amarelo e vermelho)
            Funcionam como indicadores visuais do nível de segurança:
            🟢 Verde: ambiente seguro
            🟡 Amarelo: atenção
            🔴 Vermelho: perigo
        - Display LCD
            Exibe informações como temperatura, umidade e mensagens rápidas (“seguro”, “atenção”, “perigo”).
        - Acessórios e Conexões
            Protoboard – utilizada para prototipação sem solda.
            Jumpers – empregados para interligar sensores, atuadores e a placa microcontroladora.
            
Pinagem – Conexões do Projeto
    Componente	      Pino do sensor	Pino no Pico
    HC-SR04 Trigger	      TRIG	            GP2
    HC-SR04 Echo	      ECHO	            GP3
    DHT22	              DATA	            GP18
    LED	                    +	            GP21
    Buzzer	              Sinal	            GP16
    GND Geral	            —	            GND

Como Configurar e Rodar o Projeto
    1. Acesse o Wokwi
        https://wokwi.com/
Crie um projeto com Raspberry Pi Pico.
    2. Adicione os componentes
        HC-SR04
        DHT22
        LED + resistor
        Buzzer
        Protoboard (opcional)
    3. Conecte tudo conforme a tabela de pinagem
        HC-SR04 → GP2 (Trig) e GP3 (Echo)
        DHT22 → GP18
        LED → GP21
        Buzzer → GP16
        Alimentação → 3V3 / GND / 5V
