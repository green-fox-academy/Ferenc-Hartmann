import { Component, OnInit } from '@angular/core';
import {Http} from '@angular/http';
import 'rxjs/add/operator/map';

@Component({
  selector: 'app-todo-component',
  templateUrl: './todo-component.component.html',
  styleUrls: ['./todo-component.component.css']
})

export class TodoComponentComponent implements OnInit {

  ngOnInit() {
    this.getData();
  }

  items = [];
  data = {};

  constructor(private http: Http) {
  }

  getData() {
    return this.http.get('http://localhost:3000/todo_data_get')
      .map(res => res.json())
      .subscribe(items => this.items = items);
  }


  logger = function() {
    console.log(this.items);
  }

  pushItem = function(value) {
    this.data = {};
    this.data = {
        'title': value,
        'status': 0,
    }
    this.items.push(this.data);
    // console.log(this.input.value);
    this.postData();
  };

  postData() {
    return this.http.post('http://localhost:3000/todo_data_post', this.data)
               .map(req => req.json());
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
