import { Subject } from "rxjs";

export class UsersService {
    userActivated = new Subject();
}

// A subject extends Observable - like an Ob but with the ability
// to push data to it. Subject is observable and observer at the same time

// Create it here
// Be sure to provide this subject in app.module
// in user.component, we make a function to deposit user id into this subject
// In app component, we subscribe to this Subject and retrieve the value!