import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { TodoComponentComponent } from './todo-component/todo-component.component';

@NgModule({
  declarations: [
    AppComponent,
    TodoComponentComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
