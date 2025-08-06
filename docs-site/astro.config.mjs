// @ts-check
import {defineConfig} from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({

    site: 'https://davseb21031990.github.io/plan-estudio-python-go',
    base: '/plan-estudio-python-go/',

    integrations: [
        starlight({
            title: 'Documentación',
            social: [{icon: 'github', label: 'GitHub', href: 'https://github.com/withastro/starlight'}],
            sidebar: [
                {
                    label: 'Guias',
                    items: [
                        {label: 'Intro', slug: 'guias/home'},
                        // Each item here is one entry in the navigation menu.
                        {
                            label: 'Python',
                            items: [
                                {label: 'Introducción', slug: 'guias/python/home'},
                                {label: 'Variables', slug: 'guias/python/variable'},
                                {label: 'Operadores', slug: 'guias/python/operators'},
                                {label: 'Entrada y Salidas de datos', slug: 'guias/python/input-output'},
                                {label: 'Estructuras Condicionales', slug: 'guias/python/conditionals'},
                                {label: 'Bucles', slug: 'guias/python/bucles'},
                                {label: 'Manejo de Excepciones', slug: 'guias/python/managed-exceptions'},

                                {
                                    label: 'Funciones',
                                    items: [
                                        {label: 'Introducción', slug: 'guias/python/functions/home'},
                                        {label: 'Valores de retorno', slug: 'guias/python/functions/value-return'},
                                        {label: 'Ámbito de variables', slug: 'guias/python/functions/ambito-variable'},
                                        {label: 'Argumentos predeterminados', slug: 'guias/python/functions/args-default'},
                                    ]
                                },

                                {
                                    label: 'Organización de código',
                                    items: [
                                        {label: 'Módulos', slug: 'guias/python/managed-code/modules'},
                                        {label: 'Paquetes', slug: 'guias/python/managed-code/package'},
                                        {label: 'Importaciones', slug: 'guias/python/managed-code/imports'},
                                        {label: 'Mejores Practicas para la estructura', slug: 'guias/python/managed-code/best-practices-structure'},
                                        {label: 'Dominando la gestión de dependencias', slug: 'guias/python/managed-code/mastering-dependency-management'},
                                        {label: 'Importaciones Circulares: Diagnóstico y Prevención', slug: 'guias/python/managed-code/circular-imports'},
                                    ]
                                },

                                {
                                    label: 'Colecciones',
                                    items: [
                                        {label: 'Listas', slug: 'guias/python/collections/list'},
                                        {label: 'Tuplas', slug: 'guias/python/collections/tupla'},
                                        {label: 'List Comprehensions', slug: 'guias/python/collections/list-comprehensions'},
                                        {label: 'Mejores Practicas (Listas y Tuplas)', slug: 'guias/python/collections/best-practices-list-tupla'},
                                        {label: 'Diccionarios', slug: 'guias/python/collections/dictionary'},
                                        {label: 'Conjuntos', slug: 'guias/python/collections/set'},
                                        {label: 'Mejores Practicas (Diccionarios y Conjuntos)', slug: 'guias/python/collections/best-practices-dictionary-set'},
                                    ]
                                },

                                {
                                    label: 'Programación Orientada a Objetos (POO)',
                                    items: [
                                        {label: 'Introducción', slug: 'guias/python/poo/home'},
                                        {label: 'Clases y Objetos', slug: 'guias/python/poo/class-object'},
                                        {label: 'Herencia', slug: 'guias/python/poo/inheritance'},
                                        {label: 'Sobrescritura de métodos', slug: 'guias/python/poo/override-method'},
                                        {label: 'Polimorfismo', slug: 'guias/python/poo/polymorphism'},
                                        {label: 'Composición sobre herencia', slug: 'guias/python/poo/composition-inheritance'},
                                    ]
                                },

                                {
                                    label: 'Manejo de Archivos',
                                    items: [
                                        {label: 'Introducción', slug: 'guias/python/managed-files/home'},
                                    ]
                                },

                                {
                                    label: 'Avanzado',
                                    items: [
                                        {label: 'Resolución de problemas complejos', slug: 'guias/python/advanced/solving-complex-problems'},
                                        {label: 'Entornos Virtuales', slug: 'guias/python/advanced/virtual-environments'},
                                    ]
                                },

                                {
                                    label: 'Testing',
                                    items: [
                                        {label: 'Configuración', slug: 'guias/python/testing/config'},
                                        {label: 'Conceptos Básicos', slug: 'guias/python/testing/home'},
                                        {label: 'Fixture', slug: 'guias/python/testing/fixture'},
                                        {label: 'Parametrización', slug: 'guias/python/testing/parametrizacion'},
                                        {label: 'Cobertura de código', slug: 'guias/python/testing/coverage'}
                                    ]
                                }
                            ]
                        },
                    ],
                },
                {
                    label: 'Reference',
                    autogenerate: {directory: 'reference'},
                },
            ],
        }),
    ],
});
