import { Component, OnInit, OnDestroy } from '@angular/core';
import { Observable, Observer, Subscription, interval } from 'rxjs';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit, OnDestroy {
  // Assign my observables to variables to be used by OnDestroy
  numberObservableSubscription: Subscription;
  customObservableSubscription: Subscription;

  constructor() { }

  ngOnInit() {
    // A simple observable using interval, a package from rxjs that emits numbers
    const myNumbers = interval(period: 1000)
      .pipe(map( // one of many observable operators, map maps the data you get back to a new obs with
         // any transformation you want - multiply by two in this case
        project(data: number) => {
          return data * 2;
        }
      ));
    this.numberObservableSubscription = myNumbers.subscribe(
      (number: number) => { // any name works, gotta define the type
        console.log(number);
      }
    );
    // A custom observable - Observer and type of response specified as an argument of the Observable
    const myObservable = Observable.create((observer: Observer<string>) => {
      setTimeout(() => {
        observer.next('first package'); // next simply calls the next data package
      }, 2000);
      setTimeout(() => {
        observer.next('second package');
      }, 4000);
      setTimeout(() => {
        // observer.error('fail!'); //error or complete will stop the observable
        observer.complete();
      }, 5000);
    });
    this.customObservableSubscription = myObservable.subscribe(
      // These are the three kinds of responses from Obs: data, err and complete
      // Don't need to use all of them.
      (data: string) => { console.log(data); },
      (error: string) => { console.log(error); },
      () => { console.log('finished!'); }
    )
  }

  ngOnDestroy() {
    // Should always clean up like this when you navigate away from this page, or memory leaks.
    // Angular observables should auto clean up after themselves...
    this.numberObservableSubscription.unsubscribe();
    this.customObservableSubscription.unsubscribe();
  }

}
