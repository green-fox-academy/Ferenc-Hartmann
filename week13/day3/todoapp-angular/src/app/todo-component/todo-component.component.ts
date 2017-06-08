import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-todo-component',
  templateUrl: './todo-component.component.html',
  styleUrls: ['./todo-component.component.css']
})

export class TodoComponentComponent implements OnInit {

  constructor() {}

  ngOnInit() {}

  items = ['Angular', 'React', 'Javascript'];

  pushItem = function(value) {
    this.items.push(value);
  }

  removeItem = function(index) {
    this.items.splice(index, 1);
  }

  readyCheck = function(e) {
    if (e.target.className === 'uncheck') {
      e.target.className = 'readycheck';
      console.log(e.target.className);
    }
    else if(e.target.className === 'readycheck') {
      e.target.className = 'uncheck';
      console.log(e.target.className);
    }
  }
}
