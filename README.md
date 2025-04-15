TEST - DEVELOPER - SICURANEXT

Scrivi una funzione in Python che, dato un oggetto JSON, rimuova un insieme specifico di chiavi, definite in una struttura di configurazione. Tuttavia, per alcune chiavi da rimuovere, è possibile specificare un elenco di eccezioni: se queste eccezioni sono presenti all'interno della chiave da eliminare, devono essere preservate.

Le chiavi da rimuovere e le relative eccezioni sono definite utilizzando la notazione a punti (.) per specificare il percorso all'interno della struttura JSON. La funzione deve supportare strutture JSON annidate e liste di oggetti.

Si assume che i nomi delle chiavi all'interno dell'oggetto JSON non contengano il carattere . (punto), garantendo che la notazione a punti venga utilizzata esclusivamente per la definizione dei percorsi.

Particolare attenzione sarà data all'eleganza della funzione, privilegiando una soluzione chiara, leggibile ed efficiente.
La leggibilità del codice dovrà derivare esclusivamente dalla sua chiarezza e struttura, quindi non andranno usati commenti nel codice.

Quello che segue è un esempio di funzionamento. La struttura della configurazione mostrata nell'esempio non è un requisito fisso e può essere eventualmente modificata, a condizione che continui a contenere le informazioni necessarie per specificare le chiavi da rimuovere e le relative eccezioni.

## json_data
```
{
  "id": "0001",
  "type": "donut",
  "name": "Cake",
  "ppu": [
    { "id": "1" },
    { "id": "2" }
  ],
  "batters": {
    "batter": [
      { "id": "1001", "type": "Regular", "kind": "red" },
      { "id": "1002", "type": "Chocolate", "kind": "blue" },
      { "id": "1003", "type": "Blueberry", "kind": "green" },
      { "id": "1004", "type": "Devil's Food", "kind": "yellow" }
    ],
    "name": "world"
  },
  "topping": [
    { "id": "5001", "type": "None" },
    { "id": "5002", "type": "Glazed" },
    { "id": "5005", "type": "Sugar" },
    { "id": "5007", "type": "Powdered Sugar" },
    { "id": "5006", "type": "Chocolate with Sprinkles" },
    { "id": "5003", "type": "Chocolate" },
    { "id": "5004", "type": "Maple" }
  ],
  "host": {
    "id": "1",
    "name": "test"
  },
  "machine": {
    "seq": "1",
    "os": "test"
  },
  "devices": [
    {
      "components": {
        "lists": [
          { "foo": "bar", "name": "Sugar" },
          { "foo": "pub", "name": "Maple" }        
        ]
      }
    }
  ]
}
```

## filter_keys
```
{
    "batters": ["batter.id", "batter.kind"],
    "host": ["name"],
    "devices.components": ["lists.name"],
    "machine.os": []
}
```

## Output
```
{
  "id": "0001",
  "type": "donut",
  "name": "Cake",
  "ppu": [
    {
      "id": "1"
    },
    {
      "id": "2"
    }
  ],
  "batters": {
    "batter": [
      {
        "id": "1001",
        "kind": "red"
      },
      {
        "id": "1002",
        "kind": "blue"
      },
      {
        "id": "1003",
        "kind": "green"
      },
      {
        "id": "1004",
        "kind": "yellow"
      }
    ]
  },
  "topping": [
    {
      "id": "5001",
      "type": "None"
    },
    {
      "id": "5002",
      "type": "Glazed"
    },
    {
      "id": "5005",
      "type": "Sugar"
    },
    {
      "id": "5007",
      "type": "Powdered Sugar"
    },
    {
      "id": "5006",
      "type": "Chocolate with Sprinkles"
    },
    {
      "id": "5003",
      "type": "Chocolate"
    },
    {
      "id": "5004",
      "type": "Maple"
    }
  ],
  "host": {
    "name": "test"
  },
  "machine": {
    "seq": "1"
  },
  "devices": [
    {
      "components": {
        "lists": [
          {
            "name": "Sugar"
          },
          {
            "name": "Maple"
          }
        ]
      }
    }
  ]
}
```