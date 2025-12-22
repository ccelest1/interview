# [Article](https://getbem.com/)


## Introduction
- How code is organized
    * Affects how long it takes for code to be written
    * How much of code I will have to write
    * Amount of loading/processing browser will have to perform
- Methodologies
    * Aims to reduce CSS footprint, organize cooperation, and maintain large CSS codebases
- BEM Rationale
    * Provides ample architecture with recognizable terminology
    - Blocks, Elements, Modifiers
        * Blocks
            - Standalone entity with own meaning
                * header, container, menu, checkbox, input
        * Element
            - Part of block that has no standalone meaning, tied semantically to own block
                * menu item, list item, checkbox caption, header title
        * Modifier
            - Flag on block/element -> used to change appearance or behavior
                * disabled, highlighted, checked, fixed, size big, color yellow
- Under the Hood
    * Naming rule: `block--modifier--value`
    * Example
        ```html
            <button class="button">
                Normal button
            </button>
            <button class="button button--state-success">
                Success button
            </button>
            <button class="button button--state-danger">
                Danger button
            </button>
        ```
        ```css
            .button {
                display: inline-block;
                border-radius: 3px;
                padding: 7px 12px;
                border: 1px solid #D5D5D5;
                background-image: linear-gradient(#EEE, #DDD);
                font: 700 13px/18px Helvetica, arial;
            }
            .button--state-success {
                color: #FFF;
                background: #569E3D linear-gradient(#79D858, #569E3D) repeat-x;
                border-color: #4A993E;
            }
            .button--state-danger {
                color: #900;
            }
        ```
- Benefits
    * Modularity
        - Block styles not dependent on other elements on a page
        - Can transfer blocks from finished projects to new ones
    * Reusability
        - Compose various blocks in different ways, intelligent reuse, reduce level of CSS code to be maintained
    * Structure
        - Solid structure, simple

## Naming
* Block
    - Standalone entity with own meaning -> blocks remain semantically equal
        - Naming
            * Short prefix followed by dashes, used for class selectors only
        ```html
        <div class="block"></div>
        ```
        ```css
        .block { color: #042;}
        ```
* Element
```html
<div class="block">
    <span class="block__elem"></span>
</div>
```
- Preferred
    ```css
    .block__elem { color: #042; }
    ```

* Modifier
- Flags on blocks/elements -> Used to change appearance, behavior, state
    * naming: `.block--mod` or `.block__elem--mod`
    * css: use mod class name as selector -> `.block--hidden {}`, alter elements based on block level modifier -> `.block--mod .block__elem {}`, Element modifier: `.block__elem--mod {}`
    ```html
        <div class="block block--mod"></div>
        <div class="block block--size-big block--shadow-yes "></div>
    ```
    ```css
        .block {}
        .block--mod {}
        .block--size-big {}
        .block--shadow-yes {}
    ```
* Example
```html
    <form class="form form--theme-xmas form--simple">
    <input class="form__input" type="text" />
    <input
        class="form__submit form__submit--disabled"
        type="submit" />
    </form>
```
```css
.form { }
.form--theme-xmas { }
.form--simple { }
.form__input { }
.form__submit { }
.form__submit--disabled { }
```
## FAQ Notes
