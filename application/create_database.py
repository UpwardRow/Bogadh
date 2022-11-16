from application import db, app
from application.models import Customer, Route

with app.app_context():
    db.drop_all()
    db.create_all()

    # my_dictionary = {'BusRider': 'A03', 'WheelerMann': 'A21', 'TravelGav': 'B05'}
    my_dictionary = {'BusRider': 'A03'}

    # Seems like I'm doing the same thing over and over, try to create a function
    busrider_customer = [{'customer_username': 'BusRider',
                          'email': 'phoneyadam@gmail.com',
                          'payment_type': 'PayPal',
                          'password': 'sDsad723s',
                          'first_name': 'Adam',
                          'last_name': 'Downey'
                          }
                         ]

    wheelermann_customer = [{'customer_username': 'WheelerMann',
                             'email': 'mrexample2022@gmail.com',
                             'payment_type': 'Debit Card',
                             'password': 'fsda111164534D',
                             'first_name': 'Walton',
                             'last_name': 'Mann'
                             }
                            ]

    travelgav_customer = [{'customer_username': 'TravelGav',
                           'email': 'inboxcrook@hotmail.com',
                           'payment_type': 'Credit Card',
                           'password': 'SADgSD2111i-#',
                           'first_name': 'Gavin',
                           'last_name': 'Dempsey'
                           }
                          ]


    def customer_data_insert(customer_information):
        for cust in customer_information:
            customer = Customer(customer_username=cust['customer_username'],
                                email=cust['email'],
                                payment_type=cust['payment_type'],
                                password=cust['password'],
                                first_name=cust['first_name'],
                                last_name=cust['last_name']
                                )
            db.session.add(customer)
        db.session.commit()

    # The function is being called three times, putting information for three customers into the database
    customer_data_insert(busrider_customer)
    customer_data_insert(wheelermann_customer)
    customer_data_insert(travelgav_customer)

    belfast_route = [{'route_id': 'R01',
                      'bus_id': 'NI01',
                      'destination_address': 'BELFAST, CO.ANTRIM',
                      'origin_address': 'DUBLIN, CO. DUBLIN'
                      }
                     ]

    galway_route = [{'route_id': 'R02',
                     'bus_id': 'E01',
                     'destination_address': 'GALWAY, CO.GALWAY',
                     'origin_address': 'DUBLIN, CO. DUBLIN'
                     }
                    ]

    cork_route = [{'route_id': 'R03',
                   'bus_id': 'E02',
                   'destination_address': 'CORK, CO.CORK',
                   'origin_address': 'DUBLIN, CO. DUBLIN'
                   }
                  ]

    donegal_route = [{'route_id': 'R04',
                      'bus_id': 'E03',
                      'destination_address': 'DONEGAL, CO.DONEGAL',
                      'origin_address': 'DUBLIN, CO. DUBLIN'
                      }
                     ]


    def route_data_insert(route_information):
        for rou in route_information:
            route = Route(route_id=rou['route_id'],
                          bus_id=rou['bus_id'],
                          destination_address=rou['destination_address'],
                          origin_address=rou['origin_address'],
                          )
            db.session.add(route)
        db.session.commit()

    route_data_insert(belfast_route)
    route_data_insert(galway_route)
    route_data_insert(cork_route)
    route_data_insert(donegal_route)

    # Checks if the customer_username is a foreign key, which it is
    # var1 = Ticket.query.join(Customer).all()
    # for i in var1:
    #     print(i.seat_no + ' ' + i.customer.customer_username)
