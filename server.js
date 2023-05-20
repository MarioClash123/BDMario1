const { ApolloServer, gql } = require('apollo-server');

// Datos de usuarios (pueden ser almacenados en memoria o en una base de datos)
let users = [
  { id: '1', name: 'Juan', email: 'juan@example.com' },
  { id: '2', name: 'María', email: 'maria@example.com' },
];

// Definición del esquema GraphQL
const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
  }

  input CreateUserInput {
    name: String!
    email: String!
  }

  input UpdateUserInput {
    id: ID!
    name: String!
    email: String!
  }

  type Query {
    users: [User]
    user(id: ID!): User
  }

  type Mutation {
    createUser(input: CreateUserInput!): User
    updateUser(input: UpdateUserInput!): User
    deleteUser(id: ID!): User
  }
`;

// Resolvers
const resolvers = {
  Query: {
    users: () => users,
    user: (_, { id }) => users.find(user => user.id === id),
  },
  Mutation: {
    createUser: (_, { input }) => {
      const newUser = { id: String(users.length + 1), ...input };
      users.push(newUser);
      return newUser;
    },
    updateUser: (_, { input }) => {
      const userIndex = users.findIndex(user => user.id === input.id);
      if (userIndex !== -1) {
        users[userIndex] = input;
        return input;
      }
      throw new Error('Usuario no encontrado');
    },
    deleteUser: (_, { id }) => {
      const userIndex = users.findIndex(user => user.id === id);
      if (userIndex !== -1) {
        const deletedUser = users[userIndex];
        users.splice(userIndex, 1);
        return deletedUser;
      }
      throw new Error('Usuario no encontrado');
    },
  },
};

// Configuración y creación del servidor Apollo
const server = new ApolloServer({ typeDefs, resolvers });

// Iniciar el servidor
server.listen().then(({ url }) => {
  console.log(`Servidor Apollo listo en ${url}`);
});