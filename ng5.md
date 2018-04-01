# Angular 5 Cheat Sheet
- `npm install -g @angular/cli`
- `ng new app-name`
- `cd app-name`
- `ng serve --open` (the open flag opens it in the browser)
- To make a **new component**: `ng generate component name`


The page you first see is the application shell. The shell is controlled by an Angular component named `AppComponent`.

The app.component files control the project. `app.module.ts` directs traffic for the app, and needs to know what to import, etc. App-wide styles go in `app.component.css`, for example, but **global styles** go in src/styles.css

Instantiate a new class (ie hero.ts) at the top-level of /app

The **component** is the basic building block of ng. Components shouldn't fetch/save data. Components should present data and delegate data access to a **service**.

In `src/app/app.component.ts`, the **root component**:

```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root', // the HTML selector used in index.html
  templateUrl: './app.component.html', // path to component's **template file**...
  styleUrls: ['./app.component.css'] // and css
})
export class AppComponent {
  title = 'app';
}
```

`@Component`, above, is a decorator function that specifies the Angular metadata for the component. A decorator modifies a component before its usage.



Our component contains:
```
export class CardComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
```
**Constructor** runs before data is passed to the component and **ngOnInit** runs when first cycle changes data. So use constructor for things being hard-coded into the component and use ngOnInit for everything that depends on external data.


To switch an Angular project from CSS to SASS:
- Edit `.angular-cli.json`, changing the 'css' in `apps { styles: [ styles.css ]` and `defaults: { styleExt }` to 'scss'
- Change extensions of regular .css files to .scss

To add Bootstrap to an Angular project:
- Get dependencies: `npm install --save jquery popper.js`
- Get bootstrap: `npm install --save bootstrap`
- Import it into `src/styles.scss` - `@import "../node_modules/bootstrap/scss/bootstrap";`

Or, in `angular-cli.json`:
```
-    "styles": [
        "../node_modules/bootstrap/dist/css/bootstrap.min.css",
        "styles.css"
      ],
```


[Angular CLI Wiki](https://github.com/angular/angular-cli/wiki)

**Interface** - Defines what's inside an object. Interfaces are contracts. Once you define it, TS throws an error if you don't respect it.


`<h1>{{title}}</h1>` - Double braces are ng interpolation binding syntax

Add optional features in app.module.ts like this: 
- `import { FormsModule } from '@angular/forms';` //  NgModel lives here
- ngModel is for two-way data-binding
- also, add FormsMoudle under imports in the same file. This used to be standard in earlier versions of the CLI, but no more!
- Ex `<input [(ngModel)]="hero.name" placeholder="name">` (note the brackets) - updates the name in the model and on display on the page

Use assets folder for static assets like pictures, and enviroments for env vars


**Service** to handle data fetching and sending. `ng generate service name`
