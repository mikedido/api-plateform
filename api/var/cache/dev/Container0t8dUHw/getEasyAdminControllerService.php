<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;
use Symfony\Component\DependencyInjection\Exception\RuntimeException;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'EasyCorp\Bundle\EasyAdminBundle\Controller\EasyAdminController' shared autowired service.

include_once $this->targetDirs[3].'/vendor/symfony/framework-bundle/Controller/ControllerTrait.php';
include_once $this->targetDirs[3].'/vendor/symfony/framework-bundle/Controller/AbstractController.php';
include_once $this->targetDirs[3].'/vendor/easycorp/easyadmin-bundle/src/Controller/AdminControllerTrait.php';
include_once $this->targetDirs[3].'/vendor/easycorp/easyadmin-bundle/src/Controller/EasyAdminController.php';

$this->services['EasyCorp\\Bundle\\EasyAdminBundle\\Controller\\EasyAdminController'] = $instance = new \EasyCorp\Bundle\EasyAdminBundle\Controller\EasyAdminController();

$instance->setContainer((new \Symfony\Component\DependencyInjection\Argument\ServiceLocator($this->getService, [
    'doctrine' => ['services', 'doctrine', 'getDoctrineService', false],
    'easyadmin.autocomplete' => ['services', 'easyadmin.autocomplete', 'getEasyadmin_AutocompleteService.php', true],
    'easyadmin.config.manager' => ['services', 'easyadmin.config.manager', 'getEasyadmin_Config_ManagerService', false],
    'easyadmin.filter.registry' => ['services', 'easyadmin.filter.registry', 'getEasyadmin_Filter_RegistryService', false],
    'easyadmin.paginator' => ['services', 'easyadmin.paginator', 'getEasyadmin_PaginatorService.php', true],
    'easyadmin.property_accessor' => ['services', 'easyadmin.property_accessor', 'getEasyadmin_PropertyAccessorService', false],
    'easyadmin.query_builder' => ['services', 'easyadmin.query_builder', 'getEasyadmin_QueryBuilderService.php', true],
    'easyadmin.security.authorization_checker' => ['services', 'easyadmin.security.authorization_checker', 'getEasyadmin_Security_AuthorizationCheckerService.php', true],
    'event_dispatcher' => ['services', 'event_dispatcher', 'getEventDispatcherService', false],
    'form.factory' => ['services', 'form.factory', 'getForm_FactoryService.php', true],
    'http_kernel' => ['services', 'http_kernel', 'getHttpKernelService', false],
    'parameter_bag' => ['privates', 'parameter_bag', 'getParameterBagService', false],
    'request_stack' => ['services', 'request_stack', 'getRequestStackService', false],
    'router' => ['services', 'router', 'getRouterService', false],
    'security.authorization_checker' => ['services', 'security.authorization_checker', 'getSecurity_AuthorizationCheckerService', false],
    'security.csrf.token_manager' => ['services', 'security.csrf.token_manager', 'getSecurity_Csrf_TokenManagerService.php', true],
    'security.token_storage' => ['services', 'security.token_storage', 'getSecurity_TokenStorageService', false],
    'serializer' => ['services', 'serializer', 'getSerializerService', false],
    'session' => ['services', 'session', 'getSessionService.php', true],
    'twig' => ['services', 'twig', 'getTwigService.php', true],
], [
    'doctrine' => '?',
    'easyadmin.autocomplete' => '?',
    'easyadmin.config.manager' => '?',
    'easyadmin.filter.registry' => '?',
    'easyadmin.paginator' => '?',
    'easyadmin.property_accessor' => '?',
    'easyadmin.query_builder' => '?',
    'easyadmin.security.authorization_checker' => '?',
    'event_dispatcher' => '?',
    'form.factory' => '?',
    'http_kernel' => '?',
    'parameter_bag' => '?',
    'request_stack' => '?',
    'router' => '?',
    'security.authorization_checker' => '?',
    'security.csrf.token_manager' => '?',
    'security.token_storage' => '?',
    'serializer' => '?',
    'session' => '?',
    'twig' => '?',
]))->withContext('EasyCorp\\Bundle\\EasyAdminBundle\\Controller\\EasyAdminController', $this));

return $instance;
