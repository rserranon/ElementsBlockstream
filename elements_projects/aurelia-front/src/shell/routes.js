export default [
  {
    name: 'home',
    route: ['', 'home'],
    moduleId: 'home/home',
    nav: true,
    title: 'Home',
    settings: { iconClass: 'fa-home' }
  },
  {
    route: 'bitcoin',
    moduleId: 'bitcoin/bitcoin',
    nav: true,
    settings: { iconClass: 'fa-btc' }
  },
  {
    name: 'thread',
    route: 'tickets/:id',
    moduleId: 'tickets/thread'
  },
  {
    name: 'assets',
    route: ['users', 'users/:id'],
    moduleId: 'users/users',
    href: '#users',
    nav: true,
    title: 'Users',
    settings: { iconClass: 'fa-university' }
  },
  {
    name: 'settings',
    route: 'settings',
    moduleId: 'settings/index',
    href: '#settings',
    nav: true,
    settings: { iconClass: 'fa-cog' }
  },
  {
    name: 'help',
    route: 'help',
    moduleId: 'help/help'
  }
];
