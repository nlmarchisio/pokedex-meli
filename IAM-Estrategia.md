# 🔒 Estrategia IAM para Kimberly.sas

Kimberly.sas es una empresa con operaciones en múltiples países de Latinoamérica, con más de 100,000 usuarios y más de 500 aplicaciones, incluyendo soluciones internas y comerciales. Esta estrategia de Identidad y Gestión de Accesos (**IAM - Identity & Access Management**) busca garantizar la seguridad en los siguientes aspectos:

## ✅ **Objetivos de Seguridad**
1. **Asegurar la conexión de las diferentes sedes** (identidades y accesos unificados).
2. **Asegurar la autenticación de los usuarios** en todas las aplicaciones.
3. **Garantizar la autorización adecuada de usuarios** (accesos y restricciones según roles).
4. **Asegurar los dispositivos utilizados por los usuarios** (endpoint security).
5. **Garantizar una gestión segura de usuarios administradores**.

---

## 🔹 **Estrategia IAM General**
Para garantizar la seguridad de identidad y acceso en Kimberly.sas, se propone la implementación de un **modelo centralizado de gestión de identidades** basado en **Zero Trust y principios de mínimo privilegio**.

### **🔑 1. Autenticación y Federaciones de Identidad**
📌 **Solución propuesta:** Implementación de **SSO (Single Sign-On)** con un **IdP centralizado** como **Azure AD, Okta o CyberArk**.  

- **SSO + Multi-Factor Authentication (MFA)** para todas las aplicaciones.
- **Federación con protocolos estándar:** OIDC, SAML, SCIM, LDAP para interoperabilidad.
- **Uso de autenticación sin contraseña (Passwordless)**.
- **Implementación de CyberArk como solución de autenticación segura y gestión de identidades**.

### **🛡️ 2. Autorización y Control de Acceso**
📌 **Solución propuesta:** Implementación de **RBAC + ABAC (Role-Based Access Control y Attribute-Based Access Control)**.

- **RBAC:** Definición de roles preestablecidos con permisos específicos.
- **ABAC:** Aplicación de reglas dinámicas en base a contexto (dispositivo, ubicación, riesgo).
- **Principio de Mínimo Privilegio (PoLP):** Los usuarios solo tienen acceso a lo estrictamente necesario.
- **Revisión periódica de accesos:** Auditorías semestrales para eliminar accesos innecesarios.
- **Implementación de SailPoint para la gestión centralizada del ciclo de vida de identidades y cumplimiento normativo.**

### **📱 3. Seguridad de Dispositivos y Endpoint Protection**
📌 **Solución propuesta:** **MDM (Mobile Device Management) + EDR (Endpoint Detection & Response)**.

- Implementación de **Microsoft Intune** para gestionar dispositivos.
- **Requerimiento de dispositivos de confianza** (corporativos o autenticados con certificaciones).
- **Monitoreo continuo con herramientas EDR** (CrowdStrike, SentinelOne) para detectar amenazas.

### **🛑 4. Protección de Cuentas Administrativas**
📌 **Solución propuesta:** Implementación de un **PAM (Privileged Access Management)**.

- **Gestión de cuentas con CyberArk o HashiCorp Vault**.
- **Sesiones administradas con grabación y revisión** para evitar abuso de privilegios.
- **Autenticación reforzada (MFA y claves de hardware) para usuarios con privilegios**.

---

## 🔹 **Integración de la aplicación "P@yroll"**
Dado que la aplicación **P@yroll** maneja información sensible de nóminas, se aplicarán medidas adicionales.

### **⚙️ 1. Componentes para la integración**
📌 **Se propone conectar la aplicación P@yroll al IdP centralizado** mediante:  
- **SAML 2.0 / OIDC para autenticación delegada** (SSO).
- **Uso de SCIM para sincronización de usuarios y roles**.
- **Restricción del acceso solo al departamento de contabilidad**.

### **🔒 2. Controles de Seguridad Adicionales**
- **MFA obligatorio** para los usuarios de P@yroll.
- **Autorización basada en roles (RBAC) estricta** para evitar accesos innecesarios.
- **Monitoreo de accesos con SIEM (Security Information and Event Management)**.
- **Seguridad en tránsito y en reposo** (TLS 1.2+ y cifrado de base de datos AES-256).

---

## 🔹 **Resumen de Controles Implementados**
| Control | Descripción |
|---------|------------|
| **SSO con MFA** | Autenticación unificada con segundo factor obligatorio. |
| **RBAC + ABAC** | Accesos limitados por roles y atributos contextuales. |
| **MDM y EDR** | Protección de dispositivos contra amenazas. |
| **PAM para admins** | Protección de cuentas con acceso privilegiado. |
| **SIEM para auditoría** | Monitoreo centralizado de accesos y eventos de seguridad. |
| **Integración P@yroll** | Autenticación delegada y restricción de accesos. |
| **CyberArk para autenticación** | Implementación de CyberArk como IdP y gestión de identidad. |
| **SailPoint para IGA** | Gestión del ciclo de vida de identidades y cumplimiento normativo. |

---

## 🔹 **Conclusión**
La estrategia IAM propuesta para Kimberly.sas sigue los principios de **Zero Trust, mínimo privilegio y autenticación fuerte**. Al integrar **P@yroll** de manera segura, reducimos riesgos operativos sin afectar la experiencia del usuario.

📌 **Resultado esperado:**  
✅ Seguridad centralizada con menor fricción.  
✅ Menos riesgos de accesos indebidos o fraudes.  
✅ Mejor cumplimiento normativo (GDPR, ISO 27001, SOC 2).  

---

## 📬 **Contacto**
📧 Email: nlmarchisio93@gmail.com  
💼 LinkedIn: [linkedin.com/in/nlmarchisio93](https://www.linkedin.com/in/nlmarchisio93/)  
🚀 GitHub: [github.com/nlmarchisio](https://github.com/nlmarchisio)

