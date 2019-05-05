import {inject, Aurelia} from 'aurelia-framework';
import routes from './routes';

export class Shell {
  constructor(aurelia) {
		this.aurelia = aurelia
  }

  configureRouter(config, router) {
    this.router = router;
    config.map(routes);
  }
}
