# Angular 5 Cheat Sheet
- `npm install -g @angular/cli`
- `ng new app-name`
- `cd app-name`
- `ng serve --open`

The **component** is the basic building block of ng

In `src/app/app.component.ts`, the **root component**:

```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root', // the HTML selector used in index.html
  templateUrl: './app.component.html', // path to component's html...
  styleUrls: ['./app.component.css'] // and css
})
export class AppComponent {
  title = 'app';
}
```

`@Component`, above, is a decorator function that specifies the Angular metadata for the component. A decorator modifies a component before its usage.

To make a new component: `ng generate component heroes`

To switch an Angular project from CSS to SASS:
- Edit `.angular-cli.json`, changing the 'css' in `apps { styles: [ styles.css ]` and `defaults: { styleExt }` to 'scss'
- Change extensions of regular .css files to .scss

To add Bootstrap to an Angular project:
- Get dependencies: `npm install --save jquery popper.js`
- Get bootstrap: `npm install --save bootstrap`
- Import it into `src/styles.scss` - `@import "../node_modules/bootstrap/scss/bootstrap";`

[Angular CLI Wiki](https://github.com/angular/angular-cli/wiki)

**Interface** - Defines what's inside an object. Interfaces are contracts. Once you define it, TS throws an error if you don't respect it.









