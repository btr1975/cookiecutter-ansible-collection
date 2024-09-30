# Built in Templates

### Templates directory required layout

* The folders are laid out so templates can be found from most specific to lease specific 

```text

└── templates
    └── nos
        └── solution
        |   └── family
        |   |   └── model
        |   |   |   └── template
        |   |   |
        |   |   └── main
        |   |       └── template
        |   |
        |   └── main
        |       └── template    
        |
        └── family
        |   └── model
        |   |   └── template
        |   |    
        |   └── main
        |       └── template
        |        
        └── main
            └── template
```

### Templates directory example

* Example shows a template called ntp.j2 That can be more specific for a family of devices or a specific model number
  with a catch all for the entire NOS.

```text

└── templates
    └── ios                          <-- The nos folder
        └── C3560                    <-- The family folder
        |   └── WS-C3560G-48TS-E     <-- The model folder
        |   |   └── ntp.j2
        |   |    
        |   └── main                 <-- The Catch all folder for the family **IF NEEDED**
        |       └── ntp.j2
        |        
        └── main                     <-- The Catch all folder for the entire nos
            └── ntp.j2
```
