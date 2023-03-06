using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Carbon.Identity.Data.Migrations.IdentityServer.ConfigurationDb
{
    /// <inheritdoc />
    public partial class dataclientSecrestadd : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 7, 25, 46, 275, DateTimeKind.Utc).AddTicks(5850));

            migrationBuilder.UpdateData(
                table: "ClientPostLogoutRedirectUris",
                keyColumn: "Id",
                keyValue: 2,
                column: "PostLogoutRedirectUri",
                value: "http://localhost:6002/docs/");

            migrationBuilder.UpdateData(
                table: "ClientRedirectUris",
                keyColumn: "Id",
                keyValue: 4,
                column: "RedirectUri",
                value: "https://carbon-api.azurewebsites.net/docs/oauth2-redirect");

            migrationBuilder.InsertData(
                table: "ClientSecrets",
                columns: new[] { "Id", "ClientId", "Created", "Description", "Expiration", "Type", "Value" },
                values: new object[] { 1, 2, new DateTime(2023, 3, 6, 7, 25, 46, 275, DateTimeKind.Utc).AddTicks(6430), null, null, "SharedSecret", "Radeon1GB#" });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DeleteData(
                table: "ClientSecrets",
                keyColumn: "Id",
                keyValue: 1);

            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 7, 9, 23, 239, DateTimeKind.Utc).AddTicks(2510));

            migrationBuilder.UpdateData(
                table: "ClientPostLogoutRedirectUris",
                keyColumn: "Id",
                keyValue: 2,
                column: "PostLogoutRedirectUri",
                value: "http://localhost:6002/swagger/");

            migrationBuilder.UpdateData(
                table: "ClientRedirectUris",
                keyColumn: "Id",
                keyValue: 4,
                column: "RedirectUri",
                value: "https://carbon-api.azurewebsites.net/swagger/oauth2-redirect.html");
        }
    }
}
