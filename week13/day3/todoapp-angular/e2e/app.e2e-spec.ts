import { TodoappAngularPage } from './app.po';

describe('todoapp-angular App', () => {
  let page: TodoappAngularPage;

  beforeEach(() => {
    page = new TodoappAngularPage();
  });

  it('should display welcome message', done => {
    page.navigateTo();
    page.getParagraphText()
      .then(msg => expect(msg).toEqual('Welcome to app!!'))
      .then(done, done.fail);
  });
});
