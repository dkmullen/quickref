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

// -----------------------------------------------------------------------------------
// Some notes from mean-course: Comment out to keep from breaking THIS app
// From posts.service

// a new rxjs Subject (an 'emitter') with an array of posts as a payload
private postsUpdated = new Subject<{posts: Post[], postCount: number}>();

// Gets called later in the getPosts() function
// here the Subject 'emits' the post list with 'next()' rather than 'emit
this.postsUpdated.next({posts: [...this.posts], postCount: transformedPostData.maxPosts});

// and there is also this
  // postsUpdated is private so it can only be used in this service, but the following
  // lets us retrieve it in other places for listening, such as in post-list component in ngOnInit
  getPostUpdateListener() {
    return this.postsUpdated.asObservable();
  }

  // then in post-list component, we import the service, then use the Subject like this
   // register this Sub as a var so it can be destroyed
   private postsSub: Subscription;

    // in ngOnInit we fetch the observable from posts.service and subscribe to it - be sure to unsubscribe too...
    this.postsSub = this.postsService.getPostUpdateListener()
    .subscribe((postData: {posts: Post[], postCount: number}) => {
        this.isLoading = false;
        this.totalPosts = postData.postCount;
        this.posts = postData.posts;
    });
// and then
    ngOnDestroy() {
    this.postsSub.unsubscribe();
    this.authStatusSub.unsubscribe();
    }