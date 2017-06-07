import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TodoComponentComponent } from './todo-component.component';

describe('TodoComponentComponent', () => {
  let component: TodoComponentComponent;
  let fixture: ComponentFixture<TodoComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TodoComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TodoComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
