import React from 'react';
import { Tabs } from 'expo-router';
import { View, Image, StyleSheet } from 'react-native';
import { TabBarIcon } from '@/components/navigation/TabBarIcon';
import { ThemedText } from '@/components/ThemedText';
import { Colors } from '@/constants/Colors';
import { useColorScheme } from '@/hooks/useColorScheme';

const CustomHeader = () => {
  return (
    <View style={styles.headerContainer}>
      <ThemedText type='subtitle'>MiGanado</ThemedText>
      <Image
        source={require('@/assets/images/MiGanado_logo.png')}
        style={styles.logo}
        resizeMode="contain"
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    // backgroundColor: '#FF5733', // Cambia el color aquí
  },
  headerContainer: {
    flexDirection: 'row',
    alignItems: 'flex-end',
    justifyContent: 'center',
    height: 95,
    padding: 12,
    gap: 10,
    // backgroundColor: '#FF5733',
  },
  logo: {
    width: 30,
    height: 30,
    marginRight: 10,
  },
});

export default function TabLayout() {
  const colorScheme = useColorScheme();

  return (
    <View style={styles.container}>
      <Tabs
        initialRouteName="home"
        screenOptions={{
          tabBarActiveTintColor: '#ffffff',
          tabBarInactiveTintColor: '#605856',
          headerShown: true,
          header: () => <CustomHeader />,
          tabBarShowLabel: false,
          tabBarStyle: {
            backgroundColor: '#EEEEEE',
            borderTopWidth: 0,
            elevation: 0,
            height: 80,
            paddingTop: 12
          },
        }}
      >
        <Tabs.Screen
          name="estadisticas"        
          options={{
            title: 'Estadísticas',
            tabBarIcon: ({ color, focused }) => (
              <TabBarIcon name={focused ? 'chart' : 'chart'} color={color} focused={focused} />
            ),
          }}
        />

        <Tabs.Screen
          name="notificaciones"
          options={{
            title: 'Notificaciones',
            tabBarIcon: ({ color, focused }) => (
              <TabBarIcon name={focused ? 'bell' : 'bell'} color={color} focused={focused} />
            ),
          }}
        />

        <Tabs.Screen
          name="home"
          options={{
            title: 'Home',
            tabBarIcon: ({ color, focused }) => (
              <TabBarIcon name={focused ? 'home' : 'home'} color={color} focused={focused} />
            ),
          }}
        />
        
        <Tabs.Screen
          name="lotes"
          options={{
            title: 'Lotes',
            tabBarIcon: ({ color, focused }) => (
              <TabBarIcon name={focused ? 'map' : 'map'} color={color} focused={focused} />
            ),
          }}
        />

        <Tabs.Screen
          name="perfil"
          options={{
            title: 'Perfil',
            tabBarIcon: ({ color, focused }) => (
              <TabBarIcon name={focused ? 'user' : 'user'} color={color} focused={focused} />
            ),
          }}
        />      
      </Tabs>
    </View>
  );
}
