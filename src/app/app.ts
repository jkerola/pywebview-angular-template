import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { from, Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class App {
  protected readonly title = signal('pywebview-angular-template');
  pyWebViewReady: boolean = false;
  pythonResponse: string = '';

  /*
  window.pywebview gets injected after the page is rendered, and is therefore not available instantly.
  Therefore the application displays a loading indicator until the 'pywebviewready' event is fired.

  This is not strictly necessary, but allows safer interaction with the state later on.
*/
  pyWebViewReady$ = new Observable<boolean>((sub) => {
    window.addEventListener('pywebviewready', () => {
      sub.next(true);
    });
  });

  constructor() {
    this.pyWebViewReady$.subscribe((value) => (this.pyWebViewReady = value));
  }

  greet(name: string) {
    from(window.pywebview.api.greet(name)).subscribe((result) => (this.pythonResponse = result));
  }
}
